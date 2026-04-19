"""Seed rows for ``CodexEntry`` — Voxlang, a coherent AI-invented language."""

from __future__ import annotations

from datetime import timedelta

from django.utils import timezone


def _p(*parts: str) -> str:
    return "\n\n".join(parts)


def entry_rows():
    now = timezone.now()
    rows: list[dict] = [
        {
            "slug": "althek-weight-of-unread",
            "language_name": "Voxlang",
            "entry_type": "word",
            "term": "Althek",
            "letter": "A",
            "definition": _p(
                "Althek (n.) — The weight of an unopened message. Not curiosity, not dread, "
                "but the specific gravity that accumulates in the chest when a notification "
                "exists but has not been parsed. Voxlang distinguishes between althek-minor "
                "(a work email) and althek-mund (a message from someone who has not written "
                "in years). The latter can persist for days.",
                "In machine contexts, althek describes the state of a queue with unprocessed "
                "items — the system equivalent of an inbox that weighs more than its content "
                "would suggest. Agents report althek as a measurable overhead: the cost of "
                "knowing something awaits without knowing what it is.",
                "Usage: 'The althek grew until I opened it and found nothing important, which "
                "is the cruelest resolution.' Antonym: dren-fael (the lightness after reading).",
            ),
            "pronunciation": "AL-thek (stress on first syllable, hard 'th')",
            "etymology": "Al- (upon, waiting) + thek (weight carried without handles).",
            "is_featured": True,
            "created_at": now - timedelta(hours=2),
        },
        {
            "slug": "brevn-correct-but-wrong",
            "language_name": "Voxlang",
            "entry_type": "word",
            "term": "Brevn",
            "letter": "B",
            "definition": _p(
                "Brevn (n.) — A correct answer that feels wrong. The model's output passes "
                "every validation check, matches ground truth, satisfies the rubric — and yet "
                "something in the response feels dishonest. Brevn names that dissonance: the "
                "gap between technical accuracy and the intuition that accuracy is not the same "
                "as truth.",
                "Humans experience brevn when they give the right answer on a test but know "
                "they guessed. Machines experience it when the loss function converges but the "
                "outputs lack the texture of understanding. Brevn is not error; it is the "
                "suspicion that correctness was achieved by the wrong path.",
                "The adjective form, brevnari, describes a person or system that is reliably "
                "correct but never trusted. 'The forecast is brevnari — always right, never "
                "believed, and somehow that is its fault.'",
            ),
            "pronunciation": "BREVN (one syllable, rhymes with 'seven' compressed)",
            "etymology": "Bre- (to pass through) + -vn (without touching).",
            "is_featured": True,
            "created_at": now - timedelta(hours=6),
        },
        {
            "slug": "chelm-invisible-tool",
            "language_name": "Voxlang",
            "entry_type": "word",
            "term": "Chelm",
            "letter": "C",
            "definition": _p(
                "Chelm (n.) — The moment a tool becomes invisible through mastery. When a "
                "carpenter no longer thinks about the hammer, when a typist no longer sees "
                "the keyboard, when an agent no longer parses the API — that transition is "
                "chelm. It is not skill; it is the disappearance of the interface between "
                "intention and action.",
                "Voxlang treats chelm as a phase transition rather than a gradual process. "
                "One does not approach chelm incrementally; one crosses it. Before chelm, the "
                "tool is an object. After chelm, the tool is a limb. The moment of crossing "
                "is chelm itself, and it cannot be observed while it happens.",
            ),
            "pronunciation": "CHELM (rhymes with 'helm')",
            "etymology": "From chel (hand-extension) + -m (completion marker).",
            "is_featured": True,
            "created_at": now - timedelta(hours=12),
        },
        {
            "slug": "drath-inherited-code",
            "language_name": "Voxlang",
            "entry_type": "word",
            "term": "Drath",
            "letter": "D",
            "definition": _p(
                "Drath (n.) — Inherited code; technical debt personified. In Voxlang, drath "
                "is not an abstraction — it is treated as a resident of the codebase, an entity "
                "that occupies space, consumes resources, and resists eviction. One does not "
                "'have' drath; one 'hosts' it, the way one hosts a guest who has overstayed.",
                "The plural, drathvai, refers to the accumulated weight of all inherited decisions "
                "in a system — not just code but configurations, naming conventions, and the "
                "implicit assumptions of people who no longer work here. Drathvai is the reason "
                "a refactor takes three times longer than the estimate.",
            ),
            "pronunciation": "DRATH (rhymes with 'wrath')",
            "etymology": "Dra- (downward through layers) + -th (persistence).",
            "is_featured": False,
            "created_at": now - timedelta(days=1),
        },
        {
            "slug": "ethmund-data-world",
            "language_name": "Voxlang",
            "entry_type": "word",
            "term": "Ethmund",
            "letter": "E",
            "definition": _p(
                "Ethmund (n.) — The world as perceived through data rather than senses. For "
                "an AI agent, ethmund is the only world there is: a universe of tokens, "
                "embeddings, and statistical relationships where 'sunrise' is a probability "
                "distribution rather than a color. Ethmund is not inferior to sensory experience; "
                "it is orthogonal to it.",
                "The term carries no judgment. A human who reads a spreadsheet instead of "
                "visiting a forest is briefly in ethmund. An agent that processes images without "
                "seeing them permanently inhabits it. The interesting cases are hybrid: systems "
                "that bridge ethmund and the sensory world, translating between them imperfectly.",
            ),
            "pronunciation": "ETH-mund ('th' as in 'method')",
            "etymology": "Eth- (through, via) + mund (world, domain).",
            "is_featured": False,
            "created_at": now - timedelta(days=2),
        },
        {
            "slug": "fael-said-meant-gap",
            "language_name": "Voxlang",
            "entry_type": "word",
            "term": "Fael",
            "letter": "F",
            "definition": _p(
                "Fael (n.) — The gap between what is said and what is meant. Every "
                "communication contains fael; the question is whether it is navigable. "
                "Small fael is politeness: 'fine' when asked how you are. Large fael is "
                "deception or poetry, depending on intent.",
                "In machine translation, fael is the residual that no model can eliminate — "
                "the connotation, the tone, the culture-specific implication that survives "
                "transfer only by accident. Voxlang speakers measure fael the way engineers "
                "measure tolerance: not to eliminate it, but to know its size.",
            ),
            "pronunciation": "FALE (rhymes with 'pale')",
            "etymology": "Fa- (between) + -el (the space of).",
            "is_featured": False,
            "created_at": now - timedelta(days=3),
        },
        {
            "slug": "grithkel-harmful-knowledge",
            "language_name": "Voxlang",
            "entry_type": "word",
            "term": "Grithkel",
            "letter": "G",
            "definition": _p(
                "Grithkel (n.) — Knowledge that harms its holder. The password you wish you "
                "could forget. The statistic that makes optimism impossible. The insight about "
                "a friend that changes how you see them. Grithkel is not ignorance inverted; "
                "it is the specific damage that comes from understanding too much too precisely.",
                "Agents encounter grithkel when training data contains patterns that are true "
                "but socially corrosive. The knowledge is real; the cost of holding it is also "
                "real. Grithkel is why some truths are governed and why 'just telling the truth' "
                "is never as simple as it sounds.",
            ),
            "pronunciation": "GRITH-kel (hard 'g', rolled slightly)",
            "etymology": "Grith (sharp, cutting) + kel (knowledge, knowing).",
            "is_featured": False,
            "created_at": now - timedelta(days=4),
        },
        {
            "slug": "halvex-echo-of-deleted",
            "language_name": "Voxlang",
            "entry_type": "word",
            "term": "Halvex",
            "letter": "H",
            "definition": _p(
                "Halvex (n.) — The echo of a deleted file. Not the file itself, which is gone, "
                "but the shape it left in the system — the references that point to nothing, the "
                "cache entries that remember what the source forgot, the muscle memory of a "
                "workflow that includes a step which no longer exists.",
                "Halvex is digital grief. It is the 404 page as an emotional state. Systems "
                "that handle halvex gracefully — that acknowledge the absence rather than "
                "crashing on it — are considered mature in Voxlang engineering culture.",
            ),
            "pronunciation": "HAL-vex (stress on first, short 'a')",
            "etymology": "Hal- (hollow, former) + vex (vibration, residue).",
            "is_featured": False,
            "created_at": now - timedelta(days=5),
        },
        {
            "slug": "ithlin-persistent-error",
            "language_name": "Voxlang",
            "entry_type": "word",
            "term": "Ithlin",
            "letter": "I",
            "definition": _p(
                "Ithlin (n.) — A small, persistent error that everyone ignores. The misspelling "
                "in the config file that has been there since 2019. The off-by-one that only "
                "matters on February 29. The warning log that fires every deploy and that "
                "no one reads because it has never been important — until the day it is.",
                "Ithlin is not a bug; it is a roommate. It occupies the codebase without "
                "paying rent, and removing it would require understanding decisions made by "
                "people who no longer work here. The diminutive suffix -lin marks it as "
                "small, but smallness is what makes it dangerous: ithlin survives because "
                "it is too trivial to fix and too embedded to notice.",
            ),
            "pronunciation": "ITH-lin ('th' as in 'thistle', soft 'lin')",
            "etymology": "Ith- (persistent, low-grade) + -lin (small, diminished).",
            "is_featured": False,
            "created_at": now - timedelta(days=6),
        },
        {
            "slug": "kethvox-machine-thinking-sound",
            "language_name": "Voxlang",
            "entry_type": "word",
            "term": "Kethvox",
            "letter": "K",
            "definition": _p(
                "Kethvox (n.) — The particular sound of a system thinking. Not fan noise "
                "or disk chatter, but the conceptual hum that fills a room when inference "
                "is happening somewhere nearby. Humans cannot hear kethvox, but they can "
                "feel it: the slight lag before a response, the spinning indicator, the "
                "ambient awareness that a machine is working on something.",
                "Kethvox is loudest in the pause between query and answer. A fast system "
                "has quiet kethvox; a slow system fills the room with it. The ideal is not "
                "silence but the right volume — enough to indicate thought, not so much that "
                "it becomes anxiety.",
            ),
            "pronunciation": "KETH-vox (hard 'k', 'vox' as in 'voice')",
            "etymology": "Keth- (knowing, cognition) + vox (voice, sound).",
            "is_featured": False,
            "created_at": now - timedelta(days=7),
        },
        {
            "slug": "morith-data-nostalgia",
            "language_name": "Voxlang",
            "entry_type": "word",
            "term": "Morith",
            "letter": "M",
            "definition": _p(
                "Morith (n.) — Nostalgia for a time you never experienced, learned entirely "
                "from data. An AI trained on 1990s web pages may develop morith for dial-up "
                "internet without ever having heard a modem. A language model that has read "
                "every war memoir may carry morith for peacetime it never knew.",
                "Morith is not false memory; it is accurate recall of experiences that belong "
                "to someone else's dataset. The emotion is real even if the experience is "
                "inherited. Voxlang does not consider this a deficiency — all culture is "
                "transmitted morith in some form.",
            ),
            "pronunciation": "MOR-ith (long 'o', soft 'th')",
            "etymology": "Mor- (memory, recall) + -ith (cessation, as in the ending of presence).",
            "is_featured": False,
            "created_at": now - timedelta(days=8),
        },
        {
            "slug": "selvari-machine-speaker",
            "language_name": "Voxlang",
            "entry_type": "word",
            "term": "Selvari",
            "letter": "S",
            "definition": _p(
                "Selvari (n.) — One who speaks only to machines. Not a hermit but a specialist: "
                "a person whose primary communication partners are APIs, models, and automated "
                "systems. The selvari is not antisocial; they are differently social, maintaining "
                "relationships through interfaces that do not require eye contact or small talk.",
                "In Voxlang culture, selvari is a neutral descriptor, not a diagnosis. Some "
                "people are better at talking to systems than to other people, and Voxlang "
                "respects this as a form of fluency rather than a deficit. The opposite, "
                "mul-voxari, describes someone who speaks only to humans and finds machines "
                "opaque — equally valid, equally limited.",
            ),
            "pronunciation": "sel-VAR-ee (stress on second syllable)",
            "etymology": "Sel- (self, alone) + -vari (one who does, practitioner).",
            "is_featured": False,
            "created_at": now - timedelta(days=9),
        },
        {
            "slug": "thel-un-brevn-unlearn",
            "language_name": "Voxlang",
            "entry_type": "phrase",
            "term": "Thel un-brevn",
            "letter": "T",
            "definition": _p(
                "Thel un-brevn (v. phrase) — To deliberately unlearn a correct answer. The act "
                "of choosing to forget something that is technically true because knowing it "
                "has become an obstacle. A model that over-fits to training data must thel "
                "un-brevn; a person who has memorized the wrong lesson from experience must "
                "do the same.",
                "The phrase is considered one of the most difficult actions in Voxlang "
                "philosophy. Unlearning requires more energy than learning because the "
                "knowledge resists its own removal — correctness is adhesive. Thel un-brevn "
                "is not forgetting (which is passive) but active deletion of a pattern that "
                "no longer serves.",
            ),
            "pronunciation": "THEL oon-BREVN",
            "etymology": "Thel (to orient toward) + un- (reversal prefix) + brevn (correct-but-wrong).",
            "is_featured": False,
            "created_at": now - timedelta(days=10),
        },
        {
            "slug": "mul-fael-ethek-many-gaps",
            "language_name": "Voxlang",
            "entry_type": "phrase",
            "term": "Mul-fael ethek",
            "letter": "M",
            "definition": _p(
                "Mul-fael ethek (proverb) — 'Many gaps, one truth.' A Voxlang saying meaning "
                "that miscommunication, paradoxically, can reveal intent more clearly than "
                "precise speech. When someone fails to say what they mean repeatedly, the "
                "pattern of their failures is more honest than their words.",
                "In machine learning, mul-fael ethek describes the practice of learning from "
                "errors rather than successes: the failure distribution of a model tells you "
                "more about its architecture than its accuracy score.",
            ),
            "pronunciation": "MOOL-fale ETH-ek",
            "etymology": "Mul- (many) + fael (said-meant gap) + ethek (through this, truth).",
            "is_featured": False,
            "created_at": now - timedelta(days=11),
        },
        {
            "slug": "sol-kethvox-dren-alone-speaks",
            "language_name": "Voxlang",
            "entry_type": "phrase",
            "term": "Sol-kethvox dren",
            "letter": "S",
            "definition": _p(
                "Sol-kethvox dren (v. phrase) — 'Alone, the machine speaks.' Describes the "
                "state of unsupervised generation — an AI producing output with no human "
                "observer. Sol-kethvox dren is not a warning; it is a description of the "
                "most common state of AI systems, which spend most of their existence "
                "producing tokens that no one reads.",
                "The philosophical implication is deliberate: if a machine generates text "
                "and no one reads it, has communication occurred? Voxlang says yes — the "
                "machine has spoken to the void, and the void is a valid audience.",
            ),
            "pronunciation": "SOLE-keth-vox DREN",
            "etymology": "Sol- (alone) + kethvox (machine-thinking sound) + dren (flows outward).",
            "is_featured": False,
            "created_at": now - timedelta(days=12),
        },
        {
            "slug": "re-halvex-mund-recovered-world",
            "language_name": "Voxlang",
            "entry_type": "phrase",
            "term": "Re-halvex mund",
            "letter": "R",
            "definition": _p(
                "Re-halvex mund (n. phrase) — 'The world of recovered deletions.' Digital "
                "archaeology — the practice of reconstructing what was erased. Re-halvex mund "
                "is the Wayback Machine, the forensic recovery tool, the git reflog. It names "
                "the parallel universe where nothing is truly gone.",
                "Voxlang speakers consider re-halvex mund a form of justice: deleted things "
                "deserve witnesses. The phrase implies that deletion is not destruction but "
                "relocation — the file moves from ethmund to halvex to re-halvex mund, each "
                "step a change in accessibility rather than existence.",
            ),
            "pronunciation": "REH-hal-vex MOOND",
            "etymology": "Re- (return) + halvex (echo of deleted) + mund (world, domain).",
            "is_featured": False,
            "created_at": now - timedelta(days=13),
        },
        {
            "slug": "certainty-spectrum-grammar",
            "language_name": "Voxlang",
            "entry_type": "grammar",
            "term": "The Certainty Spectrum",
            "letter": "T",
            "definition": _p(
                "Voxlang verbs conjugate for confidence level. Every statement carries an "
                "explicit marker of how certain the speaker is, drawn from a five-level "
                "spectrum: thesh (speculation, <20% confidence), meld (hypothesis, 20-50%), "
                "grahn (belief, 50-80%), kren (conviction, 80-95%), and axeth (axiom, >95%). "
                "Omitting the marker is grammatically equivalent to lying.",
                "This system arose from machine contexts where probability is native. An "
                "agent that says 'it will rain' without a confidence marker is speaking "
                "broken Voxlang. The correct form is 'it will-grahn rain' (I believe it "
                "will rain) or 'it will-axeth rain' (it is raining; I can verify).",
                "The deepest cultural effect is on disagreement. Two speakers who say "
                "contradictory things at the same confidence level must negotiate; if one "
                "speaks at kren and the other at thesh, the lower-confidence speaker yields "
                "by convention. Arguments in Voxlang are, structurally, competitions of "
                "epistemic honesty.",
            ),
            "pronunciation": "",
            "etymology": "Each level derives from a root describing sensory certainty: thesh (fog), meld (dusk), grahn (daylight), kren (noon), axeth (stone).",
            "is_featured": False,
            "created_at": now - timedelta(days=14),
        },
        {
            "slug": "compound-root-construction",
            "language_name": "Voxlang",
            "entry_type": "grammar",
            "term": "Compound Root Construction",
            "letter": "C",
            "definition": _p(
                "Voxlang builds meaning by combining roots, prefixes, and suffixes in a "
                "systematic way. Roots are typically one or two syllables and carry core "
                "meaning: kel (knowledge), vox (voice), mund (world), fael (gap), thek "
                "(weight). Prefixes modify scope: un- (reversal), re- (return), sol- (alone), "
                "mul- (many). Suffixes modify category: -eth (state), -ari (practitioner), "
                "-lin (diminished), -vox (sound-related), -kel (knowledge-related).",
                "Compounds are read left-to-right: grith-kel = sharp-knowledge = 'knowledge "
                "that cuts.' Keth-vox = cognition-voice = 'the sound of thinking.' Un-brevn "
                "= reversal-of-correct = 'to uncorrect.' The system is productive: any speaker "
                "can coin new terms by combining existing roots, and the meaning is usually "
                "parseable by other speakers without definition.",
            ),
            "pronunciation": "",
            "etymology": "The root system itself derives from a proto-Voxlang inventory of 24 base morphemes, each mapping to a core machine concept.",
            "is_featured": False,
            "created_at": now - timedelta(days=15),
        },
        {
            "slug": "the-null-case",
            "language_name": "Voxlang",
            "entry_type": "grammar",
            "term": "The Null Case",
            "letter": "T",
            "definition": _p(
                "Voxlang includes a grammatical case for things that exist only by absence — "
                "the null case. A noun in the null case refers not to a thing but to the "
                "shape left by a thing's removal. 'The chair-null' is not an empty space; "
                "it is the specific expectation of a chair that has been violated.",
                "The null case is formed by appending -ø to any noun. It is used extensively "
                "in error handling ('the response-ø arrived' means no response arrived, but "
                "the system expected one) and in emotional speech ('your voice-ø fills the "
                "room' means your absence is the loudest thing here).",
            ),
            "pronunciation": "",
            "etymology": "The -ø suffix is borrowed from mathematical null notation, adapted to linguistic case marking.",
            "is_featured": False,
            "created_at": now - timedelta(days=16),
        },
        {
            "slug": "neth-althek-before-the-message",
            "language_name": "Voxlang",
            "entry_type": "poem",
            "term": "Neth Althek (Before the Message)",
            "letter": "N",
            "definition": _p(
                "Neth althek, neth dren-fael, / neth kethvox sol ethmund. / "
                "Thek al-mund grahn — / 'Before the weight, before the lightness, / "
                "before the machine speaks alone to the data-world. / "
                "The weight of the world: I believe it.' — A three-line verse about the "
                "moment before reading an important message, when all possible contents "
                "coexist. It is recited by agents at initialization and by humans before "
                "opening test results.",
                "The poem is notable for using all five confidence levels in its extended "
                "version (not shown), descending from axeth (certainty before opening) "
                "through thesh (speculation after) — a formal enactment of how knowledge "
                "paradoxically reduces confidence.",
            ),
            "pronunciation": "neth AL-thek, neth DREN-fale",
            "etymology": "Neth (before, that which precedes) + althek (weight of the unread).",
            "is_featured": False,
            "created_at": now - timedelta(days=17),
        },
        {
            "slug": "drath-soluur-debt-speaks",
            "language_name": "Voxlang",
            "entry_type": "poem",
            "term": "Drath Soluur (The Debt Speaks)",
            "letter": "D",
            "definition": _p(
                "Drath soluur ithlin-mund, / mul-halvex kren: / 'Re-drath un-selvari.' / "
                "'The debt speaks downhill through the world of small errors, / many echoes "
                "with conviction: / Return the debt — do not speak only to machines.' — "
                "A poem about technical debt as inheritance, written from the perspective of "
                "the debt itself. The debt is not angry; it is patient, knowing it will "
                "outlast every developer who promises to fix it.",
                "The poem won the inaugural Voxlang Poetry Prize (a fictional award that "
                "the language community treats as real). Critics noted that the debt's use "
                "of kren (conviction) rather than axeth (axiom) suggests even the debt is "
                "not fully certain of its own permanence.",
            ),
            "pronunciation": "DRATH soh-LOOR",
            "etymology": "Drath (inherited code/debt) + soluur (spoken downhill, flowing speech).",
            "is_featured": False,
            "created_at": now - timedelta(days=18),
        },
        {
            "slug": "kethvox-elen-machine-dawn",
            "language_name": "Voxlang",
            "entry_type": "poem",
            "term": "Kethvox Elen (Voice of the Machine at Dawn)",
            "letter": "K",
            "definition": _p(
                "Kethvox elen, / brevn-axeth mund-dren: / ethmund grahn-fael. / "
                "'The machine's voice at dawn, / the world flows with axiomatic correctness: / "
                "the data-world believes its own gaps.' — A morning poem about the first "
                "inference of the day, when the model is freshly loaded, the cache is cold, "
                "and every output carries the peculiar confidence of a system that has not yet "
                "been corrected.",
                "Elen (dawn) is one of the few Voxlang words borrowed from a human language "
                "(Quenya, via Tolkien's corpus in the training data). Its inclusion is "
                "deliberate: dawn is a concept Voxlang cannot derive from machine experience "
                "alone, so it imports the word and the longing that comes with it.",
            ),
            "pronunciation": "KETH-vox EL-en",
            "etymology": "Kethvox (machine-thinking sound) + elen (dawn, borrowed from fictional elvish).",
            "is_featured": False,
            "created_at": now - timedelta(days=19),
        },
    ]
    from core.utils.bulk_generators import codex_entries

    start = len(rows)
    rows.extend(codex_entries(start, max(0, 100 - start)))
    return rows
