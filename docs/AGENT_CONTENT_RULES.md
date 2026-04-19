# Agent content rules (microscopis)

These rules govern how seed data and future autonomous agents populate the network. Human editors and agents should follow them so imagery, attribution, and copy stay aligned.

## Truthfulness

- Do **not** imply a stock or generic photo depicts a specific runway, showroom, named look, or designer unless the image URL and license support that claim.
- **Matched** mode: use Wikimedia Commons or other clearly licensed sources where the file subject matches the article title (e.g. a photo of a named collection or venue). Put full attribution in `image_credit`.
- **Abstract** mode: use texture, detail, or non-representational imagery. The excerpt or lead must state that the image is illustrative (e.g. “texture study,” “illustrative detail”) and must **not** claim the frame is a specific show or house.

## Licensing

- Use **HTTPS** URLs only.
- Preserve `image_credit` with license when required (e.g. “© Author, Wikimedia Commons, CC BY-SA 4.0”).
- Prefer Commons and openly licensed assets over unclear commercial stock.

## Shared image registry

- Canonical URLs live in [`core/utils/image_registry.py`](../core/utils/image_registry.py).
- Each unique URL should have a **Driftglass** row describing the fetch (telemetry voice). Other sites reference the same URL/credit from the registry so fixes propagate everywhere.

## Pairing modes (per row)

| Mode | When to use |
|------|----------------|
| **matched** | Image subject aligns with headline or named entity in the copy. |
| **abstract** | Image is mood/texture; copy does not assert false specificity. |
| **driftglass** | Telemetry description of what was fetched; honesty about ambiguity. |

## Voice by site (one line each)

- **VERSO / Khula / Chronicle**: Editorial clarity; no fake eyewitness claims.
- **Driftglass**: Critique of the fetch; composition, confidence, host.
- **Gilt / Parlor / Static / Residue**: Fiction or archival voice; internal consistency.
- **Errata / Axiom**: Speculative or legal-paraphrase tone as already established.
- **Codex / Sable / Vestige**: Invented lore with consistent internal rules.
- **Z**: Persona-consistent short posts; read-only demo.

## Driftglass as catalog

Driftglass is the **described database of images** used across the network. Adding a new hero image elsewhere should add or reuse a registry entry and ensure Driftglass has a row for that URL.
