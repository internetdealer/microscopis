# Site seed matrix

| Site | Model / focus | Target rows | Pairing / notes | Seed module | Command |
|------|----------------|------------|-----------------|-------------|---------|
| verso | VersoArticle | ~100 | matched / abstract heroes via registry | sites/verso/seed_data.py | seed_verso |
| chronicle | ChronicleEntry | ~100 | registry images | sites/chronicle/seed_data.py | seed_chronicle |
| khula | KhulaArticle | ~100 | registry + abstract where needed | sites/khula/seed_data.py | seed_khula |
| driftglass | DriftglassImage | unique URLs in registry | telemetry; one row per registry URL | sites/driftglass/seed_data.py | seed_driftglass |
| gilt | GiltEntry | ~100 | fiction | sites/gilt/seed_data.py | seed_gilt |
| parlor | ParlorDialogue | ~100 | fiction | sites/parlor/seed_data.py | seed_parlor |
| static | StaticSignal | ~100 | fiction | sites/static/seed_data.py | seed_static |
| residue | ResidueFragment | ~100 | archive fiction | sites/residue/seed_data.py | seed_residue |
| errata | ErrataCorrection | ~100 | speculative | sites/errata/seed_data.py | seed_errata |
| axiom | AxiomLaw | ~100 | governance paraphrase | sites/axiom/seed_data.py | seed_axiom |
| codex | CodexEntry | ~100 | surreal lexicon | sites/codex/seed_data.py | seed_codex |
| sable | SableTheory | ~100 | conspiracy fiction | sites/sable/seed_data.py | seed_sable |
| vestige | VestigeExhibit | ~100 | archive fiction | sites/vestige/seed_data.py | seed_vestige |
| z | Post (+ users) | ~100 posts | personas | sites/z/seed_data.py | seed_z |

Shared URLs: [`core/utils/image_registry.py`](../../core/utils/image_registry.py).
