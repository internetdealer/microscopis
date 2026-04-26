# Sourcing real hero images for VERSO and Khula (self-hosted)

## Bulk web corpus (staging / development)

The project can fill **~1300+** `IngestedArticle` rows via `python manage.py ingest_web_corpus` (see [`config/web_ingest/feeds.yaml`](../config/web_ingest/feeds.yaml) and [DEPLOY.md](../DEPLOY.md)). Seeds then map that text (and any downloaded hero) into all ~100-row sites. **Copyright, robots.txt, and terms of use** for third-party content are your compliance responsibility: this path is not a substitute for editorial or legal review on a public site.

The **licensed, hand-picked** workflow below remains the recommended approach for small, intentional hero choices.

This section below is for **humans and agents** who want **high-quality, topic-matched** hero images: pick a **licensed** or clearly reusable file, download it into `MEDIA_ROOT` under `sourced/…`, and write **new** copy that truthfully matches what the image shows.

## Rules (read [AGENT_CONTENT_RULES](AGENT_CONTENT_RULES.md) first)

1. **Do not** use images from random news or commercial sites unless you have **verifiable** rights (CC, Wikimedia, press kit, your own work, or clear terms allowing reuse and attribution).
2. **Copy** must be **original** on the site: synthesis, analysis, new structure—not a republished or lightly rephrased source article.
3. **Matched** honesty: the headline and lead should not say the image is a specific runway, venue, or product **unless** the file actually depicts that and the license allows that claim.
4. **Attribution** is mandatory: set `sourced_image_credit` (in seed) or pass `--credit` to `ingest_sourced_hero` with a full line (e.g. author, “Wikimedia Commons,” license).

## Steps

1. **Pick a direct image URL** (HTTPS) from an allowed source (default allowlist: Wikimedia upload hosts, Unsplash; see `SEED_SOURCED_IMAGE_ALLOW_HOSTS` in [DEPLOY.md](../DEPLOY.md)).
2. **Ingest** (writes `media/sourced/{verso|khula}/<slug>.<ext>` and prints the same-origin `image_url` you will store):

   ```bash
   python manage.py ingest_sourced_hero --url "https://…" --site verso --slug my-article --credit "…"
   ```

3. **Option B — seed in one go:** in `ARTICLES` (or a bulk row) add `sourced_image_url` and `sourced_image_credit` for that row; `seed_verso` / `seed_khula` will download and set `image_url` + `image_credit` (sourced **wins** over synthetic for that row).

4. Re-run the site seed: `python manage.py seed_verso` (or `seed_khula` / `seed_microscopis`).

## Safety

- Downloads are **HTTPS only**, size-limited, and (unless `*`) **host-allowlisted** to avoid the app being used as an open proxy. Configure limits via env (see [DEPLOY.md](../DEPLOY.md)).
