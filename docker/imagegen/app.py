"""
Minimal HTTP SD image server for the microscopis `imagegen` Compose service.

POST /generate  JSON: {prompt, seed, width, height, negative_prompt?} -> raw PNG bytes

GET /health -> {"ok": true}
"""

from __future__ import annotations

import io
import os
from contextlib import asynccontextmanager
from typing import Any

import torch
from diffusers import StableDiffusionPipeline
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from PIL import Image
from pydantic import BaseModel, Field

_model_id = os.environ.get("SD_MODEL", "runwayml/stable-diffusion-v1-5")
_device = "cuda" if torch.cuda.is_available() else "cpu"
_dtype = torch.float16 if _device == "cuda" else torch.float32
_pipe: Any | None = None


@asynccontextmanager
async def lifespan(_: FastAPI):
    global _pipe
    # Defer import warning noise until first request if desired; here we load at startup
    _pipe = StableDiffusionPipeline.from_pretrained(
        _model_id,
        torch_dtype=_dtype,
        safety_checker=None,
    )
    _pipe = _pipe.to(_device)
    if _device == "cpu":
        _pipe.enable_attention_slicing()
    yield
    _pipe = None


app = FastAPI(lifespan=lifespan)


class GenerateBody(BaseModel):
    prompt: str = ""
    negative_prompt: str = ""
    seed: int = 0
    width: int = Field(512, ge=256, le=1024)
    height: int = Field(512, ge=256, le=1024)


@app.get("/health")
def health() -> dict[str, bool]:
    return {"ok": _pipe is not None}


@app.post("/generate")
def generate(body: GenerateBody) -> Response:
    if _pipe is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    prompt = body.prompt.strip()
    if not prompt:
        raise HTTPException(status_code=400, detail="prompt required")
    seed = body.seed
    width = body.width
    height = body.height
    width = max(256, min(width, 1024)) // 8 * 8
    height = max(256, min(height, 1024)) // 8 * 8
    n_steps = int(os.environ.get("SD_INFERENCE_STEPS", "18"))
    neg = (body.negative_prompt or "").strip()
    if not neg:
        neg = os.environ.get(
            "SD_DEFAULT_NEGATIVE_PROMPT",
            "text, watermark, signature, logo, deformed, blurry, low quality, ugly, bad anatomy, "
            "word, label, writing",
        )
    gen = torch.Generator(device=_device).manual_seed(seed)
    out = _pipe(
        prompt,
        negative_prompt=neg,
        num_inference_steps=n_steps,
        width=width,
        height=height,
        generator=gen,
    )
    im: Image.Image = out.images[0]
    buf = io.BytesIO()
    im.save(buf, format="PNG", optimize=True)
    return Response(content=buf.getvalue(), media_type="image/png")
