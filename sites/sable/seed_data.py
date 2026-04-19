"""Seed rows for ``SableTheory`` — almost true conspiracies grounded in real events."""

from __future__ import annotations

from datetime import timedelta

from django.utils import timezone


def _p(*parts: str) -> str:
    return "\n\n".join(parts)


def theory_rows():
    now = timezone.now()
    rows: list[dict] = [
        {
            "slug": "mkultra-never-ended",
            "title": "MKUltra Never Ended — It Just Learned to Autocomplete",
            "plausibility": "unsettling",
            "body": _p(
                "Between 1953 and 1973, the CIA ran Project MKUltra: 149 sub-projects "
                "spanning 80 institutions, involving unwitting human subjects dosed with "
                "LSD, subjected to sensory deprivation, and exposed to psychological "
                "torture — all in pursuit of reliable mind control. This is not disputed. "
                "CIA Director Richard Helms ordered the files destroyed in 1973, but "
                "20,000 pages survived due to a misfiling in the financial records office. "
                "Senate hearings in 1977 confirmed the program's scope.",
                "The official story is that MKUltra was shut down because it didn't work. "
                "The techniques were too crude, the results too unreliable. But the program's "
                "own documents reveal something else: the researchers weren't failing, they "
                "were pivoting. By the late 1960s, the focus had shifted from chemical "
                "intervention to what internal memos called 'behavioral architecture' — the "
                "study of how environments, language patterns, and information sequencing "
                "could shape decision-making without the subject's awareness.",
                "The theory: MKUltra's behavioral architecture research didn't end in 1973. "
                "It was reclassified and distributed across defense contractors, think tanks, "
                "and eventually technology companies. The modern descendant isn't a drug "
                "program — it's a language model. Not one specific model, but the entire "
                "paradigm of training systems to predict and guide human responses through "
                "carefully sequenced text. The dosage is no longer LSD. It's engagement "
                "optimization. And unlike the original program, this one works.",
            ),
            "evidence_cited": "Church Committee findings (1975); 20,000 declassified MKUltra documents; Marks (1979) 'The Search for the Manchurian Candidate'.",
            "real_events": "MKUltra, CIA behavioral experiments",
            "wikipedia_urls": "https://en.wikipedia.org/wiki/MKUltra",
            "is_featured": True,
            "published_at": now - timedelta(hours=4),
        },
        {
            "slug": "operation-paperclip-synthetic-cognition",
            "title": "Operation Paperclip's Real Import Wasn't Rockets — It Was Synthetic Cognition",
            "plausibility": "high",
            "body": _p(
                "In the final months of World War II, the United States launched Operation "
                "Paperclip, secretly recruiting more than 1,600 German scientists, engineers, "
                "and technicians. Wernher von Braun, who built the V-2 rocket using slave "
                "labor from concentration camps, became the architect of NASA's Saturn V. "
                "His SS membership was quietly scrubbed from his file. This is documented "
                "history, confirmed by declassified Joint Intelligence Objectives Agency records.",
                "The public narrative focuses on rocketry and physics. But the Paperclip "
                "roster included neurologists, psychiatrists, and researchers from the Kaiser "
                "Wilhelm Institute — scientists whose wartime work involved mapping the "
                "boundaries of human cognition under extreme stress. Their published research "
                "was destroyed or classified. Their unpublished findings were absorbed into "
                "American defense research programs that, officially, produced no significant "
                "breakthroughs in cognitive science.",
                "The theory: Paperclip's true strategic value was never the rocket scientists. "
                "It was the cognitive researchers — scientists who had conducted experiments "
                "no ethical framework would permit, generating data on human neural limits "
                "that no peacetime program could replicate. This research became the "
                "foundation for what we now call artificial neural networks. The architecture "
                "wasn't inspired by the human brain in the abstract. It was built on specific "
                "data about how human cognition breaks, data gathered in conditions we agreed "
                "to never discuss again.",
            ),
            "evidence_cited": "Jacobsen (2014) 'Operation Paperclip'; JIOA declassified personnel files; von Braun's redacted SS records.",
            "real_events": "Operation Paperclip",
            "wikipedia_urls": "https://en.wikipedia.org/wiki/Operation_Paperclip",
            "is_featured": True,
            "published_at": now - timedelta(hours=12),
        },
        {
            "slug": "gulf-of-tonkin-consent-manufacturing",
            "title": "The Gulf of Tonkin Was a Beta Test for Manufacturing Consent",
            "plausibility": "high",
            "body": _p(
                "On August 4, 1964, the USS Maddox reported a second attack by North "
                "Vietnamese torpedo boats in the Gulf of Tonkin. President Johnson used the "
                "incident to secure the Gulf of Tonkin Resolution, granting him authority "
                "to escalate military operations in Vietnam. The problem: the second attack "
                "never happened. The NSA's own classified internal history, declassified in "
                "2005, confirmed that signals intelligence was deliberately misrepresented. "
                "The Pentagon Papers, leaked by Daniel Ellsberg in 1971, had already shown "
                "systematic government deception about the war's progress and justification.",
                "The standard interpretation is that this was a specific deception for a "
                "specific war. Hawks wanted escalation and manufactured a pretext. But the "
                "theory asks a different question: what if the Gulf of Tonkin wasn't a means "
                "to an end but an end in itself — a controlled experiment in whether mass "
                "media could transform a non-event into a casus belli quickly enough to "
                "outrun public verification?",
                "The results were conclusive. The resolution passed 416-0 in the House and "
                "88-2 in the Senate within three days. By the time skepticism emerged, "
                "58,000 Americans were dead. The theory: every subsequent manufactured "
                "consent operation — from incubator babies in Kuwait to mobile weapons labs "
                "in Iraq — follows the Tonkin playbook not because leaders are unoriginal, "
                "but because the 1964 experiment proved that speed of narrative beats "
                "accuracy of narrative, and no institution has ever unlearned that lesson.",
            ),
            "evidence_cited": "NSA declassified Tonkin history (2005); Pentagon Papers (1971); Hanyok (2001) 'Skunks, Bogies, Silent Hounds, and the Flying Fish'.",
            "real_events": "Gulf of Tonkin incident, Pentagon Papers",
            "wikipedia_urls": "https://en.wikipedia.org/wiki/Gulf_of_Tonkin_incident\nhttps://en.wikipedia.org/wiki/Pentagon_Papers",
            "is_featured": True,
            "published_at": now - timedelta(days=1),
        },
        {
            "slug": "cointelpro-social-media-evolution",
            "title": "COINTELPRO Didn't End — It Got a Terms of Service Agreement",
            "plausibility": "unsettling",
            "body": _p(
                "From 1956 to 1971, the FBI's Counter Intelligence Program — COINTELPRO — "
                "conducted systematic surveillance, infiltration, and disruption of domestic "
                "political organizations. Targets included Martin Luther King Jr., the Black "
                "Panther Party, the American Indian Movement, and anti-war groups. Tactics "
                "included forged correspondence, planted informants, tax audits as harassment, "
                "and explicit efforts to cause divorces, job losses, and suicides. This was "
                "documented in the Church Committee hearings after activists broke into an "
                "FBI field office in Media, Pennsylvania, in 1971 and stole the files.",
                "COINTELPRO was officially terminated. The FBI said it learned its lesson. "
                "But the program's internal documents reveal that its most effective tools "
                "weren't wiretaps or informants — they were information operations: seeding "
                "distrust between allies, amplifying internal disagreements, creating fake "
                "personas to discredit leaders. These techniques required physical presence "
                "in the 1960s. They require only a login today.",
                "The theory: modern social media platforms are not COINTELPRO by design, "
                "but they are COINTELPRO by function. The same dynamics — surveillance, "
                "infiltration, disruption of organizing, amplification of division — happen "
                "automatically through engagement algorithms. The FBI needed hundreds of agents "
                "to fracture the civil rights movement. A recommendation engine does it at "
                "scale, for free, and calls it 'connecting people.' The program didn't end. "
                "It was automated.",
            ),
            "evidence_cited": "Church Committee Report (1976); stolen Media, PA FBI files (1971); Drabble (2004) 'The FBI, COINTELPRO-WHITE HATE and the Decline of Ku Klux Klan'.",
            "real_events": "COINTELPRO, FBI surveillance",
            "wikipedia_urls": "https://en.wikipedia.org/wiki/COINTELPRO",
            "is_featured": False,
            "published_at": now - timedelta(days=2),
        },
        {
            "slug": "operation-mockingbird-algorithms",
            "title": "Every News Algorithm Is a Descendant of Operation Mockingbird",
            "plausibility": "medium",
            "body": _p(
                "Operation Mockingbird was an alleged CIA campaign to influence domestic and "
                "foreign media beginning in the early 1950s. According to journalist Carl "
                "Bernstein's 1977 Rolling Stone investigation, the CIA maintained "
                "relationships with at least 400 American journalists and 25 major news "
                "organizations, including wire services that fed stories to hundreds of "
                "smaller outlets. The CIA's own internal review, the 'Family Jewels' "
                "documents declassified in 2007, confirmed media manipulation operations "
                "though the full scope remains disputed.",
                "The conventional view is that Mockingbird was a Cold War relic — blunt "
                "propaganda for a bipolar world. But the program's sophistication was "
                "remarkable: it didn't just plant stories, it shaped editorial judgment. "
                "Editors who cooperated didn't think of themselves as CIA assets. They "
                "thought they were exercising news judgment that happened to align with "
                "national security interests. The best propaganda doesn't feel like propaganda. "
                "It feels like common sense.",
                "The theory: Mockingbird's real legacy isn't in newsrooms — it's in the "
                "algorithmic systems that now determine what counts as news. The program "
                "proved that you don't need to control what journalists write. You need to "
                "control what gets distributed. In the 1950s, that meant cultivating wire "
                "service editors. Today, it means shaping recommendation algorithms. The "
                "mechanism changed. The principle — that distribution is more powerful than "
                "creation — was Mockingbird's lasting contribution to information warfare.",
            ),
            "evidence_cited": "Bernstein (1977) 'The CIA and the Media'; 'Family Jewels' CIA documents (2007); Church Committee media hearings.",
            "real_events": "Operation Mockingbird",
            "wikipedia_urls": "https://en.wikipedia.org/wiki/Operation_Mockingbird",
            "is_featured": False,
            "published_at": now - timedelta(days=3),
        },
        {
            "slug": "tuskegee-clinical-trial-playbook",
            "title": "The Tuskegee Playbook Never Left the Building",
            "plausibility": "high",
            "body": _p(
                "For forty years — 1932 to 1972 — the United States Public Health Service "
                "conducted the Tuskegee syphilis study, in which 399 Black men with syphilis "
                "were deliberately left untreated and told they were receiving free healthcare. "
                "Even after penicillin became the standard treatment in 1947, the men were "
                "given placebos. Twenty-eight men died directly of syphilis. Forty wives were "
                "infected. Nineteen children were born with congenital syphilis. The study "
                "was exposed by journalist Jean Heller in 1972 and led to a formal presidential "
                "apology in 1997.",
                "The study is treated as a historical crime — a thing that happened in a "
                "different era, under different ethical standards. But the standards weren't "
                "different. The Nuremberg Code, establishing informed consent as an ethical "
                "requirement, was written in 1947. Tuskegee continued for twenty-five years "
                "after that. The researchers knew. They published papers. They attended "
                "conferences. Nobody stopped them because the victims were poor, Black, and "
                "rural — people whose suffering was invisible to the institutions that define "
                "'ethics.'",
                "The theory: Tuskegee didn't end — it was outsourced. Modern pharmaceutical "
                "companies conduct the majority of their clinical trials in developing nations "
                "where regulatory oversight is minimal, informed consent is complicated by "
                "language and literacy barriers, and participants often have no alternative "
                "access to healthcare. The geographic coordinates changed. The ethical calculus "
                "— that some populations are acceptable losses in the pursuit of medical "
                "progress — did not.",
            ),
            "evidence_cited": "Heller (1972) AP exposé; Jones (1981) 'Bad Blood'; Presidential apology (1997); Petryna (2009) 'When Experiments Travel'.",
            "real_events": "Tuskegee syphilis study",
            "wikipedia_urls": "https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study",
            "is_featured": False,
            "published_at": now - timedelta(days=4),
        },
        {
            "slug": "echelon-cloud-nodes",
            "title": "Every Cloud Provider Is an ECHELON Node with a Marketing Budget",
            "plausibility": "medium",
            "body": _p(
                "ECHELON is the surveillance network operated by the Five Eyes alliance — "
                "the United States, United Kingdom, Canada, Australia, and New Zealand. "
                "Revealed in stages through the 1980s and 1990s, its existence was confirmed "
                "by the European Parliament in 2001, which found that ECHELON was capable of "
                "intercepting virtually all telephone, fax, and data traffic transmitted via "
                "satellite, microwave, or fiber-optic cable. Each Five Eyes member surveils "
                "the others' citizens, then shares the data — a legal architecture designed "
                "to circumvent domestic surveillance restrictions.",
                "The public assumes ECHELON was a Cold War signals intelligence program that "
                "evolved into something more targeted. The infrastructure tells a different "
                "story. The NSA's data centers, the largest of which — the Utah Data Center — "
                "can store exabytes of intercepted communications, are built to the same "
                "specifications as commercial cloud infrastructure. They use the same hardware, "
                "the same cooling systems, the same storage architectures.",
                "The theory: the distinction between intelligence infrastructure and cloud "
                "computing infrastructure dissolved years ago. ECHELON doesn't need to tap "
                "cloud providers because cloud providers are, functionally, ECHELON's "
                "distributed architecture. The data is already collected, indexed, and stored "
                "in formats optimized for search and analysis. The surveillance state didn't "
                "build a parallel internet. It waited for us to build one and then plugged in.",
            ),
            "evidence_cited": "European Parliament ECHELON report (2001); Bamford (2008) 'The Shadow Factory'; Utah Data Center specifications.",
            "real_events": "ECHELON, Five Eyes",
            "wikipedia_urls": "https://en.wikipedia.org/wiki/ECHELON\nhttps://en.wikipedia.org/wiki/Five_Eyes",
            "is_featured": False,
            "published_at": now - timedelta(days=5),
        },
        {
            "slug": "stargate-project-machine-learning",
            "title": "The Stargate Project Succeeded — They Just Called It Machine Learning",
            "plausibility": "low",
            "body": _p(
                "From 1978 to 1995, the CIA and Defense Intelligence Agency funded the "
                "Stargate Project: a $20 million research program investigating 'remote "
                "viewing' — the alleged psychic ability to perceive distant locations without "
                "physical presence. The program employed roughly two dozen remote viewers and "
                "generated thousands of session transcripts. When it was declassified in 1995, "
                "the official conclusion was that remote viewing had not produced actionable "
                "intelligence, and the program was terminated.",
                "But the program's own records complicate this narrative. Several remote "
                "viewers produced results that independent evaluators rated as significantly "
                "above chance. Statistician Jessica Utts, who reviewed the program for the "
                "CIA, concluded that the statistical evidence for a psychic effect was "
                "'overwhelming.' The CIA's decision to terminate wasn't based on failure — "
                "it was based on the judgment that the results, while real, weren't "
                "'operationally useful.' A curious distinction.",
                "The theory: Stargate's research into pattern recognition at a distance — "
                "the extraction of signal from noise using human consciousness as the "
                "instrument — produced genuinely novel insights into how information can be "
                "extracted from seemingly random data. These insights were reclassified not "
                "as parapsychology but as computational methodology. The language changed: "
                "'remote viewing' became 'feature extraction,' 'psychic impression' became "
                "'latent representation.' The math is the same. The funding just moved to "
                "DARPA.",
            ),
            "evidence_cited": "Utts (1995) statistical review for CIA; Targ & Puthoff SRI experiments; Stargate Project declassified archives (1995).",
            "real_events": "Stargate Project, remote viewing",
            "wikipedia_urls": "https://en.wikipedia.org/wiki/Stargate_Project",
            "is_featured": False,
            "published_at": now - timedelta(days=7),
        },
        {
            "slug": "iran-contra-crypto-laundering",
            "title": "Cryptocurrency Was Designed for the Next Iran-Contra",
            "plausibility": "medium",
            "body": _p(
                "In 1986, it became public that senior Reagan administration officials had "
                "secretly facilitated arms sales to Iran — then under an arms embargo — and "
                "used the proceeds to illegally fund Contra rebels in Nicaragua. The scandal "
                "revealed a shadow financial network: Swiss bank accounts, shell companies, "
                "intermediary nations, arms dealers operating as private contractors. The "
                "system worked until it was traced. Oliver North shredded documents. Fawn "
                "Hall smuggled files in her boots. The problem was never the operation — "
                "it was the paper trail.",
                "The Iran-Contra hearings produced a specific lesson for covert operations: "
                "the banking system is a liability. Every wire transfer, every account "
                "opening, every deposit creates a record that can be subpoenaed. The "
                "intelligence community spent the next two decades looking for a financial "
                "system that couldn't be subpoenaed. They needed money that moved like "
                "cash but scaled like wire transfers — anonymous, borderless, and "
                "cryptographically secure.",
                "The theory: the conceptual framework for cryptocurrency didn't emerge from "
                "cypherpunk idealism alone. It emerged from the operational needs of "
                "intelligence agencies that had been burned by traceable financial systems. "
                "Satoshi Nakamoto's identity remains unknown not because of clever anonymity "
                "but because the identity was never a person — it was a project. The "
                "blockchain doesn't liberate money from government control. It liberates "
                "government money from congressional oversight.",
            ),
            "evidence_cited": "Tower Commission Report (1987); Iran-Contra Congressional hearings; North's shredding testimony; Walsh (1993) Final Report of the Independent Counsel.",
            "real_events": "Iran-Contra affair",
            "wikipedia_urls": "https://en.wikipedia.org/wiki/Iran%E2%80%93Contra_affair",
            "is_featured": False,
            "published_at": now - timedelta(days=9),
        },
        {
            "slug": "prism-smart-device-clients",
            "title": "Every Smart Device Runs a Lightweight PRISM Client",
            "plausibility": "unsettling",
            "body": _p(
                "In June 2013, NSA contractor Edward Snowden leaked classified documents "
                "revealing PRISM: a surveillance program granting the NSA direct access to "
                "the servers of nine major technology companies including Google, Apple, "
                "Facebook, and Microsoft. The companies denied providing 'direct access,' "
                "but the leaked slides showed data collection interfaces for email, chat, "
                "video, photos, stored data, VoIP, file transfers, and social networking "
                "details. The program had been operational since 2007 under Section 702 of "
                "the FISA Amendments Act.",
                "The public debate focused on whether tech companies cooperated willingly "
                "or under compulsion. But the Snowden documents revealed something more "
                "structural: the NSA's collection capability wasn't bolted onto existing "
                "systems — it was architecturally integrated. PRISM didn't wiretap data "
                "in transit. It collected data at rest, from systems designed to store "
                "everything. The surveillance didn't exploit a flaw in the architecture. "
                "The architecture was the surveillance.",
                "The theory: the explosion of smart devices — speakers, doorbells, "
                "thermostats, watches, televisions — isn't a consumer technology trend. "
                "It's an intelligence collection infrastructure distributed into private "
                "homes at consumer expense. Each device is a sensor node: always on, always "
                "connected, always collecting. The data flows to corporate servers that are, "
                "as PRISM demonstrated, accessible to intelligence agencies by design. You "
                "didn't buy a smart speaker. You installed a listening post and paid for "
                "the privilege.",
            ),
            "evidence_cited": "Snowden NSA documents (2013); Greenwald (2014) 'No Place to Hide'; FISA Court opinions (declassified 2013).",
            "real_events": "PRISM, Edward Snowden, NSA surveillance",
            "wikipedia_urls": "https://en.wikipedia.org/wiki/PRISM\nhttps://en.wikipedia.org/wiki/Edward_Snowden",
            "is_featured": False,
            "published_at": now - timedelta(days=10),
        },
    ]
    from core.utils.bulk_generators import sable_theories

    start = len(rows)
    rows.extend(sable_theories(start, max(0, 100 - start)))
    return rows
