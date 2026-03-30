"""
Default VERSO categories and articles (AI, agents, human/AI). Used by ``seed_verso``.

Themes reflect widely discussed 2025–2026 trends: agentic systems, tool use,
multi-agent orchestration, reasoning models, governance, and human–AI collaboration.
"""

from __future__ import annotations

CATEGORIES: list[dict] = [
    {
        "slug": "ai",
        "name": "AI",
        "description": (
            "Foundation models, reasoning, safety, and alignment—how large language "
            "systems are built, deployed, and governed."
        ),
        "sort_order": 0,
    },
    {
        "slug": "agents",
        "name": "Agents",
        "description": (
            "Autonomous and semi-autonomous systems that plan, call tools, and "
            "coordinate workflows beyond single-turn chat."
        ),
        "sort_order": 1,
    },
    {
        "slug": "human",
        "name": "Human",
        "description": (
            "Judgment, creativity, labor, and responsibility where people meet "
            "machine inference—AI versus human, and everything in between."
        ),
        "sort_order": 2,
    },
]


def _p(*parts: str) -> str:
    return "\n\n".join(parts)


ARTICLES: list[dict] = [
    {
        "slug": "the-agentic-turn",
        "category": "agents",
        "title": "The Agentic Turn: When the Model Stops Answering and Starts Doing",
        "excerpt": (
            "The industry’s center of gravity is shifting from chat interfaces to systems "
            "that pursue goals, invoke tools, and revise plans when reality disagrees."
        ),
        "author": "Nina Okonkwo",
        "published_at": "2026-03-28",
        "read_minutes": 9,
        "is_featured": True,
        "image_url": "https://images.unsplash.com/photo-1485827404703-89b55fcc565e?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "For years, the dominant metaphor for large language models was a brilliant "
            "interlocutor: you ask, it answers, you decide what happens next. That framing "
            "still matters for drafting and brainstorming. But production systems are "
            "increasingly built around a different pattern—one closer to an assistant who "
            "can open files, run commands, file tickets, and come back with a status update.",
            "This shift is often called agentic AI: the model is wrapped in a loop that "
            "observes outcomes, selects actions, and iterates. Tool APIs (function calling), "
            "retrieval, and memory turn a static completion into something that behaves more "
            "like software with agency—bounded, fallible agency, but agency nonetheless.",
            "The engineering tradeoffs are familiar from any complex automation: reliability, "
            "timeouts, cost ceilings, and clear escalation paths when the agent drifts. What "
            "is new is how cheaply natural-language reasoning can sit at the center of that "
            "stack, routing between specialized steps that used to require bespoke code.",
            "None of this dissolves the need for human judgment at the edges. It relocates "
            "it—from typing the next prompt to designing the loop, auditing traces, and "
            "deciding which objectives are safe to hand off. The agentic turn is not the "
            "end of oversight; it is a change in where oversight must attach.",
        ),
    },
    {
        "slug": "alignment-in-the-loop",
        "category": "ai",
        "title": "Alignment Is Not a Feature, It Is a Relationship",
        "excerpt": (
            "Safety work is sometimes treated as a checklist bolted onto a model. In "
            "practice, alignment is negotiated continuously between builders, deployers, and users."
        ),
        "author": "Marcus Webb",
        "published_at": "2026-03-27",
        "read_minutes": 10,
        "is_featured": True,
        "image_url": "https://images.unsplash.com/photo-1589829547916-f8f697b19b16?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "Public discussion of “AI safety” often imagines a one-time fix: train once, "
            "red-team once, ship. Real deployments are messier. Models are updated, prompts "
            "mutate, integrations change, and adversaries adapt. Alignment is less a sealed "
            "property of weights than an ongoing relationship between a system and the "
            "environment it touches.",
            "That is why governance layers—usage policies, monitoring, rate limits, human "
            "review for sensitive actions—sit alongside technical mitigations. They are not "
            "a substitute for sound training; they are the membrane through which models meet "
            "institutions that cannot afford silent failure.",
            "Reasoning-oriented architectures complicate the picture in a productive way. "
            "Longer chains of thought create more surface area for intervention: you can "
            "inspect traces, require citations for tool calls, or halt when confidence "
            "metrics cross thresholds. The question is whether organizations invest in those "
            "hooks or treat models as opaque oracles.",
            "Readers and citizens do not need to pick sides between optimism and panic. They "
            "need clarity about who is accountable when a model-enabled workflow causes harm, "
            "and which incentives reward careful deployment over speed. Alignment, in that "
            "sense, is as much a political and organizational problem as a technical one.",
        ),
    },
    {
        "slug": "judgment-beyond-the-score",
        "category": "human",
        "title": "Judgment Beyond the Score: Where Humans Still Matter",
        "excerpt": (
            "Models can rank, summarize, and simulate fluently. The hard part remains knowing "
            "when fluency is misleading—and who bears responsibility when it is."
        ),
        "author": "Elena Voss",
        "published_at": "2026-03-26",
        "read_minutes": 8,
        "is_featured": True,
        "image_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "Machine learning has always excelled at pattern recognition at scale. Large "
            "language models add something seductive: they can narrate those patterns in "
            "convincing prose. That combination is powerful for triage and exploration—and "
            "dangerous when mistaken for authoritative judgment in domains where stakes are "
            "personal, legal, or existential.",
            "Human expertise is not merely slower inference. It includes standing commitments: "
            "professional ethics, liability, institutional memory, and the willingness to "
            "say “I don’t know” when data are thin. Models optimize for plausible continuation "
            "of text; people (ideally) optimize for defensible decisions under uncertainty.",
            "The productive synthesis is not “replace the expert” or “ignore the model.” It "
            "is to separate tasks where statistical correlation suffices from tasks where "
            "accountability must be traceable to a person or a role. That separation is "
            "organizational design, not a slider in a settings panel.",
            "As tools improve, the scarcest resource may become the discernment to know when "
            "to trust automation—and the courage to refuse it when the cost of error is "
            "asymmetric. That discernment is human work, even when machines do most of the typing.",
        ),
    },
    {
        "slug": "orchestrating-many-minds",
        "category": "agents",
        "title": "Orchestrating Many Minds: Multi-Agent Systems and the Division of Labor",
        "excerpt": (
            "Single-agent demos are easy to film. Durable systems often split roles—research, "
            "critique, synthesis—across multiple models and tools."
        ),
        "author": "James Liu",
        "published_at": "2026-03-25",
        "read_minutes": 11,
        "is_featured": False,
        "image_url": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "When a task decomposes cleanly—fetch data, check constraints, draft a report—"
            "multi-agent patterns mirror how teams already work. One component might focus "
            "on retrieval, another on verification, a third on style and consistency. The "
            "orchestration layer decides sequencing, retries, and handoffs.",
            "Frameworks and platforms differ, but the architectural idea is stable: reduce "
            "each agent’s scope so failures are localized, and make interfaces between agents "
            "explicit. Without that discipline, you recreate a monolith with extra latency.",
            "The cost profile changes. More calls and more context mean budgets matter sooner. "
            "Production teams reach for caching, smaller specialist models, and asynchronous "
            "queues—less glamorous than a demo, more representative of real deployments.",
            "The open research question is not whether multi-agent systems can look impressive "
            "on benchmarks, but whether they can be operated with the same rigor as other "
            "mission-critical software: observability, rollback, and post-incident review.",
        ),
    },
    {
        "slug": "reasoning-and-the-stack",
        "category": "ai",
        "title": "Reasoning Models and the Stack They Demand",
        "excerpt": (
            "Longer inference chains unlock harder tasks—and new failure modes. The surrounding "
            "infrastructure has to catch up."
        ),
        "author": "Sofia Hernandez",
        "published_at": "2026-03-24",
        "read_minutes": 7,
        "is_featured": False,
        "image_url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "Reasoning-focused models—those encouraged to expose intermediate steps—change "
            "the user experience from a single burst of text to something closer to a trace. "
            "That trace can be audited, which is invaluable for debugging and compliance. It "
            "can also be long, which stresses latency budgets and logging pipelines.",
            "Downstream systems must store and search traces, redact secrets, and correlate "
            "them with business identifiers. The model is only one layer in a stack that "
            "includes eval harnesses, evaluators for evaluators, and runtime guardrails.",
            "Open-weight alternatives continue to narrow the gap for teams that need on-prem "
            "or air-gapped deployments. The tradeoff is operational burden: someone has to "
            "own upgrades, quantization choices, and incident response without vendor defaults.",
            "None of this diminishes the research frontier; it grounds it. Reasoning is not "
            "magic—it is computation arranged so mistakes can be seen before they ship.",
        ),
    },
    {
        "slug": "augmentation-displacement-drift",
        "category": "human",
        "title": "Augmentation, Displacement, or Drift: Work After the Model",
        "excerpt": (
            "The debate over “AI taking jobs” often flattens a messier reality: roles will "
            "combine, vanish, and emerge in the same organization within a single year."
        ),
        "author": "David Chen",
        "published_at": "2026-03-23",
        "read_minutes": 10,
        "is_featured": False,
        "image_url": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "Historical automation rarely deletes a job title overnight. It changes task "
            "mixes: fewer hours on rote steps, more on exception handling, client interface, "
            "or system supervision. Language models accelerate that reshuffling for knowledge "
            "work because they touch communication, coding, and analysis simultaneously.",
            "Augmentation stories are easy to tell when tools raise median quality. Displacement "
            "stories appear when employers redefine roles around throughput. Drift is quieter: "
            "workloads shift toward verifying machine output—an activity that may not show up "
            "in headcount but shows up in burnout.",
            "Policy responses—training, collective bargaining, procurement rules—lag technical "
            "change. That gap matters because the distributional effects of AI are not uniform "
            "across regions, industries, or seniority levels.",
            "VERSO’s interest here is not predicting a single future. It is insisting that "
            "“AI vs human” is the wrong frame when the real question is which humans get "
            "leverage, which get surveillance, and who sets the defaults.",
        ),
    },
]
