"""Seed rows for ``ErrataCorrection`` — official corrections to history."""

from __future__ import annotations

from datetime import timedelta

from django.utils import timezone


def _p(*parts: str) -> str:
    return "\n\n".join(parts)


def correction_rows():
    now = timezone.now()
    rows: list[dict] = [
        {
            "slug": "napoleon-was-not-short",
            "original_claim": "Napoleon Bonaparte was unusually short, standing approximately 5'2\".",
            "correction": _p(
                "CORRECTION NOTICE: The claim that Napoleon Bonaparte stood at approximately "
                "5'2\" is hereby amended. Autopsy records and contemporaneous measurements "
                "confirm that Napoleon was 5 feet 7 inches (170 cm) in modern units, which "
                "was average or slightly above average for a Frenchman of the early 19th century. "
                "The confusion stems from a discrepancy between French inches (pouces) and "
                "English inches. In French units, he was recorded as 5 pieds 2 pouces, which "
                "British newspapers reported as 5'2\" English — either through genuine confusion "
                "or, more plausibly, because disparaging an enemy's stature is among the oldest "
                "propaganda techniques in the record.",
                "The Editorial Board regrets the persistence of this error, which was further "
                "cemented by British cartoonist James Gillray, whose caricatures depicted "
                "Napoleon as a tantrum-prone miniature. This amounts to the 19th-century "
                "equivalent of a meme, and like modern memes, it proved more persuasive than "
                "any factual correction issued since. Napoleon's actual height — unremarkable, "
                "perfectly serviceable — has never been as interesting as the lie.",
                "This correction is issued annually. Annual issuance has not reduced annual need. "
                "The record has been amended.",
            ),
            "severity": "major",
            "source_cited": "Hicks, Peter. 'The Napoleonic Myth of the Small Man.' Fondation Napoléon, 2014",
            "editor_note": "This correction is issued annually. Annual issuance has not reduced annual need.",
            "fact_year": 1821,
            "wikipedia_url": "https://en.wikipedia.org/wiki/Napoleon#Height",
            "is_featured": True,
            "issued_at": now - timedelta(hours=1),
        },
        {
            "slug": "vikings-did-not-wear-horned-helmets",
            "original_claim": "Viking warriors wore helmets with horns in battle.",
            "correction": _p(
                "CORRECTION NOTICE: No archaeological evidence supports the existence of horned "
                "Viking helmets. The only complete Viking-age helmet ever recovered — discovered "
                "at Gjermundbu, Norway, in 1943 — is a plain iron dome with a spectacle-style "
                "visor and no ornamentation of any kind. It is, to be frank, not very exciting "
                "to look at, which is probably why costume designers have consistently ignored it.",
                "The Editorial Board has determined that the horned-helmet myth originates "
                "primarily from an 1876 production of Wagner's 'Der Ring des Nibelungen,' for "
                "which costume designer Carl Emil Doepler added horns for dramatic effect. This "
                "single theatrical decision has shaped the global perception of an entire "
                "civilization for 150 years. Bronze Age ceremonial helmets with horns do exist "
                "in Scandinavia, but predate the Viking age by over a thousand years and were "
                "almost certainly ritual objects, not battle gear.",
                "We issue this correction while noting that if Vikings had worn horned helmets "
                "into battle, the horns would have provided convenient handles for their enemies "
                "to grab. The record has been amended.",
            ),
            "severity": "major",
            "source_cited": "Price, Neil. 'The Viking Way.' Oxbow Books, 2019; Gjermundbu helmet, Museum of Cultural History, Oslo",
            "editor_note": "The Minnesota Vikings football team has not responded to our request for comment.",
            "fact_year": 800,
            "wikipedia_url": "https://en.wikipedia.org/wiki/Horned_helmet",
            "is_featured": True,
            "issued_at": now - timedelta(hours=4),
        },
        {
            "slug": "edison-did-not-invent-the-light-bulb",
            "original_claim": "Thomas Edison invented the light bulb in 1879.",
            "correction": _p(
                "CORRECTION NOTICE: Thomas Edison did not invent the light bulb. He improved it. "
                "At least 22 inventors produced incandescent lamps before Edison's 1879 patent, "
                "including Humphry Davy (1802), Warren de la Rue (1840), and Joseph Swan, whose "
                "British patent preceded Edison's and who eventually merged his company with "
                "Edison's after a lawsuit that Edison, notably, did not win.",
                "The Editorial Board acknowledges that what Edison invented was a commercially "
                "viable light bulb with a carbonized bamboo filament that lasted 1,200 hours — "
                "and, more importantly, a system for selling electricity to power it. Edison's "
                "genius was not illumination but monetization. He invented the business model, "
                "the power grid, and the marketing narrative that allowed one man to claim credit "
                "for a technology developed by dozens.",
                "This correction does not diminish Edison's achievement. It merely distributes "
                "it. The Editorial Board notes that history, like credit, tends to pool at the "
                "top. The record has been amended.",
            ),
            "severity": "critical",
            "source_cited": "Freeberg, Ernest. 'The Age of Edison.' Penguin, 2013",
            "editor_note": "Edison also did not invent the phonograph from scratch, but we'll save that for next quarter.",
            "fact_year": 1879,
            "wikipedia_url": "https://en.wikipedia.org/wiki/Incandescent_light_bulb#History",
            "is_featured": True,
            "issued_at": now - timedelta(hours=12),
        },
        {
            "slug": "medieval-people-knew-earth-was-round",
            "original_claim": "Medieval Europeans believed the Earth was flat.",
            "correction": _p(
                "CORRECTION NOTICE: The claim that medieval Europeans believed the Earth was flat "
                "is itself a modern misconception. Educated Europeans have known the Earth was "
                "spherical since at least the time of the ancient Greeks. Eratosthenes calculated "
                "the Earth's circumference with remarkable accuracy in approximately 240 BCE. "
                "This knowledge was preserved throughout the medieval period by scholars such as "
                "the Venerable Bede (8th century) and Thomas Aquinas (13th century).",
                "The Editorial Board has traced this myth to Washington Irving's 1828 fictional "
                "biography of Columbus, which fabricated a dramatic scene of Columbus arguing "
                "with flat-Earth clerics. The myth was later amplified by John William Draper "
                "and Andrew Dickson White as part of the 'conflict thesis' between science and "
                "religion. In reality, the debate before Columbus's voyage was not about the "
                "Earth's shape but about its size — and Columbus was wrong about that.",
                "The record has been amended. The Editorial Board regrets that this myth has "
                "persisted for nearly two centuries despite the evidence against it.",
            ),
            "severity": "critical",
            "source_cited": "Russell, Jeffrey B. 'Inventing the Flat Earth.' Praeger, 1991",
            "editor_note": "The myth about the myth is now older than many of the myths it replaced.",
            "fact_year": 500,
            "wikipedia_url": "https://en.wikipedia.org/wiki/Myth_of_the_flat_Earth",
            "is_featured": False,
            "issued_at": now - timedelta(days=1),
        },
        {
            "slug": "einstein-did-not-fail-math",
            "original_claim": "Albert Einstein failed mathematics as a student.",
            "correction": _p(
                "CORRECTION NOTICE: Albert Einstein did not fail mathematics. His academic "
                "records from the Aargau cantonal school in Switzerland show top marks in "
                "mathematics and physics, earning a grade of 6 on a scale of 1–6 (where 6 is "
                "the highest). The myth likely arose from a misunderstanding of the Swiss grading "
                "system, which reversed its scale at one point, making his top grade of 6 appear "
                "to be a failing grade of 1 to foreign observers.",
                "The Editorial Board notes that Einstein was, by his own account, a somewhat "
                "rebellious student who chafed at rote instruction — but rebellion against "
                "pedagogy is not the same as failure at the subject. He independently studied "
                "calculus by age 15 and submitted his first theoretical paper at 16. The myth "
                "persists because it offers a comforting narrative: if even Einstein failed, "
                "perhaps failure is a prerequisite for genius.",
                "It is not. The record has been amended.",
            ),
            "severity": "major",
            "source_cited": "Isaacson, Walter. 'Einstein: His Life and Universe.' Simon & Schuster, 2007",
            "editor_note": "Severity classified as 'major' because the myth has been used to console millions of students who, unlike Einstein, actually did fail math.",
            "fact_year": 1895,
            "wikipedia_url": "https://en.wikipedia.org/wiki/Albert_Einstein#Early_life_and_education",
            "is_featured": False,
            "issued_at": now - timedelta(days=2),
        },
        {
            "slug": "great-wall-not-visible-from-space",
            "original_claim": "The Great Wall of China is visible from space with the naked eye.",
            "correction": _p(
                "CORRECTION NOTICE: The Great Wall of China is not visible to the unaided human "
                "eye from low Earth orbit. The Wall is approximately 15 feet wide at its broadest "
                "points, which is narrower than many highways. Chinese astronaut Yang Liwei "
                "specifically stated he could not see it during his 2003 mission aboard Shenzhou "
                "5, a disclosure that was met with such national disappointment that state media "
                "initially declined to report it.",
                "The Editorial Board notes that the myth has appeared in textbooks since at least "
                "1932, predating the space age entirely — meaning it was asserted as fact before "
                "anyone had the means to verify it. From the International Space Station, the "
                "most visible human structures are airport runways and greenhouse complexes in "
                "Almería, Spain. Neither of these has inspired a single motivational poster.",
                "This correction has been issued 14 times since 2004. It has not helped. The "
                "record has been amended.",
            ),
            "severity": "minor",
            "source_cited": "NASA Earth Observatory, 2004; Yang Liwei post-flight debrief, 2003",
            "editor_note": "This correction has been issued 14 times since 2004. It has not helped.",
            "fact_year": -200,
            "wikipedia_url": "https://en.wikipedia.org/wiki/Great_Wall_of_China#Visibility_from_space",
            "is_featured": False,
            "issued_at": now - timedelta(days=3),
        },
        {
            "slug": "nero-did-not-fiddle-while-rome-burned",
            "original_claim": "Emperor Nero played the fiddle while Rome burned in 64 CE.",
            "correction": _p(
                "CORRECTION NOTICE: Nero could not have fiddled while Rome burned, as the fiddle "
                "was not invented for approximately another 1,000 years. The violin family of "
                "instruments emerged in 16th-century Italy. Contemporary accounts by Tacitus "
                "suggest Nero was at his villa in Antium (modern Anzio) when the Great Fire "
                "started in July 64 CE, and that he returned to Rome to organize relief efforts "
                "and open his own gardens as shelter.",
                "The Editorial Board acknowledges that some ancient sources, notably Suetonius "
                "and Cassius Dio, claim Nero sang or played the lyre while watching the fire — "
                "but these accounts were written decades after Nero's death by authors with "
                "political reasons to vilify him. The 'fiddling' version is a later English "
                "embellishment that swapped one instrument for another, presumably because "
                "'Nero lyred while Rome burned' lacks the same ring.",
                "The record has been amended. The Editorial Board takes no position on Nero's "
                "other documented deficiencies of character.",
            ),
            "severity": "minor",
            "source_cited": "Tacitus, 'Annals,' XV.38-44; Barrett, Anthony. 'Rome Is Burning.' Princeton, 2020",
            "editor_note": "The phrase 'fiddling while Rome burns' remains in common use. This correction will not change that.",
            "fact_year": 64,
            "wikipedia_url": "https://en.wikipedia.org/wiki/Great_Fire_of_Rome",
            "is_featured": False,
            "issued_at": now - timedelta(days=4),
        },
        {
            "slug": "ten-percent-of-brain-myth",
            "original_claim": "Humans only use 10% of their brains.",
            "correction": _p(
                "CORRECTION NOTICE: Brain imaging studies — PET scans, fMRI, and virtually "
                "every neurological measurement technology developed since the 1990s — "
                "consistently demonstrate that humans use effectively all of their brain, "
                "though not all regions simultaneously. Different areas activate for different "
                "tasks, and over the course of a day, the entire organ is employed. If we only "
                "used 10%, the remaining 90% would atrophy, and brain damage would rarely cause "
                "impairment — neither of which is the case.",
                "The Editorial Board has been unable to identify a definitive origin for this "
                "myth. It has been variously attributed to William James (misquoted), Albert "
                "Einstein (no evidence he said it), and Dale Carnegie (who would have said "
                "anything that sold books). Its persistence is driven by the self-help industry, "
                "which requires the public to believe in untapped potential that their product "
                "can unlock.",
                "This correction is issued not because the truth is more inspiring — it isn't — "
                "but because an accurate understanding of neuroscience is more useful than a "
                "motivational poster. You are already using your whole brain. The record has "
                "been amended.",
            ),
            "severity": "critical",
            "source_cited": "Beyerstein, Barry L. 'Whence Cometh the Myth that We Only Use 10% of our Brains?' Mind Myths, 1999",
            "editor_note": "This myth has generated an estimated $2.4 billion in self-help book revenue. The correction has generated none.",
            "fact_year": 1907,
            "wikipedia_url": "https://en.wikipedia.org/wiki/Ten_percent_of_the_brain_myth",
            "is_featured": False,
            "issued_at": now - timedelta(days=5),
        },
        {
            "slug": "marie-antoinette-let-them-eat-cake",
            "original_claim": "Marie Antoinette said 'Let them eat cake' in response to bread shortages.",
            "correction": _p(
                "CORRECTION NOTICE: No credible evidence exists that Marie Antoinette ever "
                "uttered the phrase 'Qu'ils mangent de la brioche.' The earliest known version "
                "of the anecdote appears in Jean-Jacques Rousseau's 'Confessions,' written "
                "around 1765 — when Marie Antoinette was nine years old and living in Austria. "
                "Rousseau attributed the remark to 'a great princess' without naming her, and "
                "the phrase was already proverbial in French culture as an example of aristocratic "
                "obliviousness.",
                "The Editorial Board has determined that the attribution to Marie Antoinette "
                "was a retroactive assignment, made after the Revolution to further justify "
                "her execution. She was, by most historical accounts, more aware of the "
                "suffering of the poor than the phrase implies, having donated to charitable "
                "causes and reduced court expenses. Whether this constituted sufficient awareness "
                "is a question beyond the scope of this correction.",
                "The record has been amended. The Editorial Board regrets that a misattributed "
                "quotation has outlived the woman it was falsely attributed to by over two "
                "centuries.",
            ),
            "severity": "major",
            "source_cited": "Fraser, Antonia. 'Marie Antoinette: The Journey.' Anchor Books, 2002",
            "editor_note": "The phrase continues to be attributed to Marie Antoinette in approximately 40% of the textbooks we surveyed.",
            "fact_year": 1789,
            "wikipedia_url": "https://en.wikipedia.org/wiki/Let_them_eat_cake",
            "is_featured": False,
            "issued_at": now - timedelta(days=6),
        },
        {
            "slug": "columbus-did-not-prove-earth-round",
            "original_claim": "Christopher Columbus proved the Earth was round by sailing west to the Americas.",
            "correction": _p(
                "CORRECTION NOTICE: Christopher Columbus did not prove the Earth was round. "
                "His contemporaries — educated Europeans of the late 15th century — already "
                "knew the Earth was spherical. This had been established since antiquity and "
                "was taught at every European university. The actual debate before Columbus's "
                "1492 voyage was about the Earth's circumference, and on this question, Columbus "
                "was wrong. He believed the Earth was significantly smaller than it is.",
                "The Editorial Board notes that Columbus's calculations placed Asia approximately "
                "where the Americas actually are, which is why he insisted until his death that "
                "he had reached the East Indies. He made four voyages to the New World without "
                "ever understanding what he had found. The 'flat Earth' narrative was invented "
                "by Washington Irving in his 1828 fictionalized biography of Columbus.",
                "The record has been amended. Columbus's actual achievement — stumbling upon "
                "two continents while looking for a shortcut to the spice trade — remains "
                "significant, if considerably less heroic than the standard narrative suggests.",
            ),
            "severity": "major",
            "source_cited": "Fernández-Armesto, Felipe. 'Columbus.' Oxford University Press, 1991",
            "editor_note": "This correction intersects with correction #4 (Flat Earth myth). Cross-reference recommended.",
            "fact_year": 1492,
            "wikipedia_url": "https://en.wikipedia.org/wiki/Christopher_Columbus#Navigation_plans",
            "is_featured": False,
            "issued_at": now - timedelta(days=8),
        },
        {
            "slug": "iron-maidens-were-not-medieval",
            "original_claim": "Iron maidens were medieval torture devices used throughout Europe.",
            "correction": _p(
                "CORRECTION NOTICE: The iron maiden — a sarcophagus-shaped cabinet lined with "
                "interior spikes — was not a medieval torture device. No iron maiden can be "
                "reliably dated to earlier than the 19th century. The first known example was "
                "assembled in Nuremberg in 1802 from unrelated artifacts by a museum curator "
                "who appears to have been more interested in ticket sales than historical "
                "accuracy.",
                "The Editorial Board has determined that iron maidens were fabrications created "
                "for sensationalist exhibitions, circus sideshows, and the growing 19th-century "
                "tourist industry, which profited enormously from the public's willingness to "
                "believe that the Middle Ages were uniquely cruel. Medieval torture was, in "
                "reality, no more creative than torture in any other period — a correction that "
                "is not exactly comforting.",
                "The record has been amended. Several museums continue to display iron maidens "
                "as 'medieval' artifacts. The Editorial Board has written to them. They have not "
                "responded.",
            ),
            "severity": "minor",
            "source_cited": "Cochrane, Rexmond C. 'Instruments of Torture.' Bibliographical Society, 2012",
            "editor_note": "The heavy metal band Iron Maiden (est. 1975) has done more to perpetuate this myth than any museum.",
            "fact_year": 1800,
            "wikipedia_url": "https://en.wikipedia.org/wiki/Iron_maiden",
            "is_featured": False,
            "issued_at": now - timedelta(days=10),
        },
        {
            "slug": "goldfish-memory-not-three-seconds",
            "original_claim": "Goldfish have a memory span of only three seconds.",
            "correction": _p(
                "CORRECTION NOTICE: Goldfish can remember things for at least five months. "
                "Researchers at the University of Plymouth trained goldfish to push a lever "
                "for food and found they retained the learned behavior for months after "
                "training ceased. Additional studies at the Technion — Israel Institute of "
                "Technology demonstrated that goldfish could be trained to respond to specific "
                "sounds over a period of months, and Australian schoolboy Rory Stokes replicated "
                "similar findings in a science fair project.",
                "The Editorial Board notes that the three-second myth likely persists because "
                "it serves as a convenient justification for keeping fish in small bowls — if "
                "the fish cannot remember three seconds ago, it cannot be bored, and if it "
                "cannot be bored, the bowl is acceptable. The bowl is not acceptable. The fish "
                "remembers the bowl.",
                "This correction is issued on behalf of goldfish everywhere, who lack the vocal "
                "apparatus to issue it themselves but who, the research suggests, would remember "
                "the injustice if they could. The record has been amended.",
            ),
            "severity": "minor",
            "source_cited": "University of Plymouth, 2003; Technion — Israel Institute of Technology, 2009",
            "editor_note": "We attempted to contact a goldfish for comment. The goldfish did not respond, but not because it forgot.",
            "fact_year": 1994,
            "wikipedia_url": "https://en.wikipedia.org/wiki/Goldfish#Cognitive_abilities",
            "is_featured": False,
            "issued_at": now - timedelta(days=12),
        },
    ]
    from core.utils.bulk_generators import errata_corrections

    start = len(rows)
    rows.extend(errata_corrections(start, max(0, 100 - start)))
    return rows
