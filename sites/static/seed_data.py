"""Seed rows for ``StaticSignal`` — real numbers stations and shortwave mysteries."""

from __future__ import annotations

from datetime import timedelta

from django.utils import timezone


def _p(*parts: str) -> str:
    return "\n\n".join(parts)


CONET = "https://archive.org/details/ird059"
CONET_EMBED = "ird059"


def signal_rows():
    now = timezone.now()
    rows: list[dict] = [
        {
            "slug": "uvb-76-the-buzzer",
            "designation": "UVB-76 / 'The Buzzer'",
            "signal_type": "numbers",
            "origin_description": "4625 kHz, Russia — believed near Pskov, later relocated near Moscow",
            "transcript": _p(
                "UVB-76 has been transmitting a short, monotonous buzzing tone on "
                "4625 kHz since at least 1982. The buzz repeats roughly 25 times per "
                "minute, 24 hours a day, interrupted only by rare voice messages. "
                "Listeners worldwide have monitored the frequency for decades, "
                "cataloguing every anomaly. The station's purpose has never been "
                "officially acknowledged by the Russian government.",
                "On rare occasions — sometimes years apart — the buzzing stops and a "
                "voice reads a coded message in Russian, typically consisting of names "
                "and number groups: 'Ya UVB-76, Ya UVB-76. 93 882 naimina 74 14. "
                "Boris, Roman, Olga, Mikhail...' In 2010, activity surged with "
                "multiple voice intrusions, conversations accidentally broadcast, and "
                "what sounded like a live room with shuffling papers and distant "
                "speech — as if someone had left a microphone open in a military "
                "facility.",
                "The transmitter was traced to a Russian military installation near "
                "Povarovo, outside Moscow, which was apparently relocated around 2010. "
                "Theories range from a dead-man's switch for nuclear retaliation to a "
                "channel reservation system for Russian military communications. The "
                "buzzing continues to this day.",
            ),
            "analysis_notes": "Active since 1982. Monitored continuously by shortwave hobbyists. Voice messages documented in 1997, 2006, 2010, and sporadically since.",
            "audio_url": CONET,
            "archive_embed_id": CONET_EMBED,
            "is_featured": True,
            "intercepted_at": now - timedelta(hours=2),
        },
        {
            "slug": "lincolnshire-poacher-e03",
            "designation": "E03 / 'The Lincolnshire Poacher'",
            "signal_type": "numbers",
            "origin_description": "11.545 MHz, attributed to RAF Akrotiri, Cyprus",
            "transcript": _p(
                "The Lincolnshire Poacher was a British numbers station that "
                "broadcast on shortwave frequencies from the mid-1970s until June "
                "2008. Each transmission opened with the first two bars of the "
                "English folk song 'The Lincolnshire Poacher,' played on an "
                "electronic organ, repeated several times before a female voice with "
                "a received pronunciation accent began reading groups of five "
                "numbers.",
                "Direction-finding by amateur radio operators consistently pointed "
                "toward RAF Akrotiri, a British military base in Cyprus, though the "
                "UK government never acknowledged the station. The signal was "
                "powerful and widely received across Europe, the Middle East, and "
                "North Africa. It was one of the most well-known numbers stations "
                "during the Cold War era and remained active long after.",
                "The station ceased operations in June 2008, around the same time "
                "its sister station Cherry Ripe (E28) also went silent. Researchers "
                "believe both were operated by the Secret Intelligence Service (MI6) "
                "for communicating with agents in the field.",
            ),
            "analysis_notes": "Operated mid-1970s to June 2008. Extensively documented by The Conet Project (1997). Attributed to MI6/SIS via direction-finding.",
            "audio_url": CONET,
            "archive_embed_id": CONET_EMBED,
            "is_featured": True,
            "intercepted_at": now - timedelta(hours=6),
        },
        {
            "slug": "swedish-rhapsody-g02",
            "designation": "G02 / 'Swedish Rhapsody'",
            "signal_type": "numbers",
            "origin_description": "Shortwave, believed origin: Poland or East Germany",
            "transcript": _p(
                "The Swedish Rhapsody station is one of the most unsettling numbers "
                "stations ever documented. Transmissions opened with a music-box "
                "rendition of Hugo Alfvén's 'Swedish Rhapsody No. 1,' followed by a "
                "young girl's voice reading groups of numbers in German. The child's "
                "voice — almost certainly a synthesis or recording — gave the station "
                "an eerie quality that distinguished it from other numbers stations.",
                "The station was active during the Cold War, primarily in the 1970s "
                "and 1980s, broadcasting on various shortwave frequencies. It was "
                "categorized as a German-language station (hence the G02 designation "
                "in the ENIGMA classification system). Researchers believe it was "
                "operated by Polish or East German intelligence services to "
                "communicate with agents in Western Europe.",
                "The Swedish Rhapsody station became iconic after its inclusion in "
                "The Conet Project, a 1997 compilation of numbers station recordings "
                "released by Irdial-Discs. The track featuring the child's voice "
                "reading numbers over the music-box melody remains one of the most "
                "widely shared recordings in the numbers station community.",
            ),
            "analysis_notes": "Cold War era, primarily 1970s–1980s. Featured prominently on The Conet Project. ENIGMA designation G02.",
            "audio_url": CONET,
            "archive_embed_id": CONET_EMBED,
            "archive_embed_file": "tcp_d1_01_the_swedish_rhapsody_irdial.mp3",
            "is_featured": True,
            "intercepted_at": now - timedelta(hours=14),
        },
        {
            "slug": "yosemite-sam",
            "designation": "Undesignated / 'Yosemite Sam'",
            "signal_type": "broadcast",
            "origin_description": "~3700 kHz, Albuquerque NM area (direction-finding estimate)",
            "transcript": _p(
                "Beginning around 2004, shortwave listeners in the American Southwest "
                "reported a bizarre repeating signal near 3700 kHz. The transmission "
                "consisted of a data burst followed by a clip of the Looney Tunes "
                "character Yosemite Sam shouting 'Varmint, I'm a-gonna blow you to "
                "smithereens!' The clip and data burst repeated at regular intervals "
                "with no other content.",
                "Direction-finding efforts by multiple amateur radio operators "
                "triangulated the source to an area near Albuquerque, New Mexico, "
                "possibly near Kirtland Air Force Base or Sandia National "
                "Laboratories. The FCC investigated but never publicly identified the "
                "source or the purpose of the transmissions. The use of a cartoon "
                "audio clip suggested either a test signal, a marker, or an "
                "intentional effort to obscure the data content of the transmission.",
            ),
            "analysis_notes": "First reported ~2004. FCC investigated, source never publicly identified. Ceased sometime after 2010. Possibly a military test or research signal.",
            "audio_url": "",
            "is_featured": False,
            "intercepted_at": now - timedelta(days=1),
        },
        {
            "slug": "atencion-hm01",
            "designation": "HM01 / 'Atención'",
            "signal_type": "numbers",
            "origin_description": "Various HF frequencies, Cuba",
            "transcript": _p(
                "Atención is the common name for a Cuban numbers station that has "
                "been broadcasting since at least the 1960s. Transmissions begin with "
                "the Spanish word '¡Atención!' repeated several times, followed by a "
                "female voice reading five-figure number groups. The station uses "
                "multiple frequencies and schedules, and has been one of the most "
                "consistently active numbers stations in the Western Hemisphere.",
                "The Cuban government's use of numbers stations was confirmed during "
                "the trial of the Wasp Network (Red Avispa) in 2001, when FBI agents "
                "demonstrated that coded messages broadcast on shortwave from Cuba "
                "could be decrypted using one-time pads found in the possession of "
                "arrested Cuban intelligence agents operating in South Florida. The "
                "decrypted messages contained operational instructions for espionage "
                "activities.",
                "Despite this public exposure, the station continued broadcasting. "
                "It remains active under the ENIGMA designation HM01, serving as one "
                "of the last confirmed state-operated numbers stations whose purpose "
                "has been verified in open court.",
            ),
            "analysis_notes": "Active since at least the 1960s. Cuban intelligence link confirmed in the 2001 Wasp Network trial. Still broadcasting as of recent monitoring.",
            "audio_url": CONET,
            "archive_embed_id": CONET_EMBED,
            "is_featured": False,
            "intercepted_at": now - timedelta(days=2),
        },
        {
            "slug": "cherry-ripe-e28",
            "designation": "E28 / 'Cherry Ripe'",
            "signal_type": "numbers",
            "origin_description": "HF shortwave, attributed to Australian facility linked to MI6",
            "transcript": _p(
                "Cherry Ripe was a British numbers station that used the opening bars "
                "of the traditional English song 'Cherry Ripe' as its interval "
                "signal. Like its sister station The Lincolnshire Poacher, it "
                "employed a female voice reading five-figure number groups in "
                "English. The station broadcast primarily on high-frequency shortwave "
                "bands targeting the Asia-Pacific region.",
                "Direction-finding placed the transmitter in Australia, likely at a "
                "joint UK-Australian signals intelligence facility. Researchers "
                "believe Cherry Ripe was operated by MI6 as a companion to The "
                "Lincolnshire Poacher, covering a different geographic area with the "
                "same communications protocol. Both stations served as one-way "
                "broadcast channels to intelligence agents in the field.",
                "Cherry Ripe ceased operations around the same time as The "
                "Lincolnshire Poacher in 2008, suggesting a coordinated shutdown of "
                "the network — possibly replaced by digital communications methods.",
            ),
            "analysis_notes": "Operated until ~2008. Sister station to E03 (Lincolnshire Poacher). Believed MI6, transmitting from Australia. Shut down concurrently with E03.",
            "audio_url": CONET,
            "archive_embed_id": CONET_EMBED,
            "is_featured": False,
            "intercepted_at": now - timedelta(days=3),
        },
        {
            "slug": "the-pip-s28",
            "designation": "S28 / 'The Pip'",
            "signal_type": "unknown",
            "origin_description": "3756 kHz, Russia",
            "transcript": _p(
                "The Pip is a Russian signal station that transmits continuous short "
                "pip tones at approximately one-second intervals on 3756 kHz. Like "
                "its better-known counterpart UVB-76 (The Buzzer), The Pip is "
                "believed to be a Russian military channel marker — a signal that "
                "reserves a frequency for potential use and can be interrupted for "
                "voice communications when needed.",
                "Occasionally, the pipping stops and is replaced by voice messages in "
                "Russian, typically consisting of callsigns and number groups similar "
                "to those heard on UVB-76. These voice intrusions are rare and "
                "unpredictable. Listeners have also reported hearing background "
                "sounds — distant conversations, machinery, radio chatter — bleeding "
                "through during transitions, suggesting a live facility rather than "
                "an automated transmitter.",
            ),
            "analysis_notes": "Active. Continuously monitored by shortwave hobbyists. Paired with UVB-76 and S32 (The Squeaky Wheel) as Russian channel-marker stations.",
            "audio_url": "",
            "is_featured": False,
            "intercepted_at": now - timedelta(days=5),
        },
        {
            "slug": "the-conet-project",
            "designation": "'The Conet Project' — Recordings of Shortwave Numbers Stations",
            "signal_type": "broadcast",
            "origin_description": "Worldwide shortwave recordings, compiled 1993–1997",
            "transcript": _p(
                "The Conet Project is a four-CD compilation of recordings of numbers "
                "stations from around the world, released in 1997 by the London-based "
                "label Irdial-Discs. It contains over four hours of recordings "
                "collected by shortwave radio enthusiasts between 1993 and 1997, "
                "documenting dozens of different stations broadcasting in English, "
                "German, Spanish, Czech, Russian, and other languages.",
                "The compilation was among the first widely available collections of "
                "numbers station recordings and played a significant role in bringing "
                "public attention to the phenomenon. It was released under a free "
                "distribution license, and the recordings were later uploaded to the "
                "Internet Archive, where they remain freely accessible. Artists "
                "including Wilco (who sampled it on 'Yankee Hotel Foxtrot') and "
                "Boards of Canada have drawn on the recordings.",
                "The project's liner notes include an essay on the history of numbers "
                "stations, their suspected use by intelligence agencies for one-way "
                "communication with field agents via one-time pad encryption, and the "
                "legal ambiguity surrounding their operation — stations that are "
                "clearly government-run yet officially denied by every nation.",
            ),
            "analysis_notes": "Released 1997 by Irdial-Discs. Free on the Internet Archive. Sampled by Wilco on 'Yankee Hotel Foxtrot' (2001). Foundational document for numbers station research.",
            "audio_url": CONET,
            "archive_embed_id": CONET_EMBED,
            "is_featured": False,
            "intercepted_at": now - timedelta(days=7),
        },
    ]
    from core.utils.bulk_generators import static_signals

    start = len(rows)
    rows.extend(static_signals(start, max(0, 100 - start)))
    return rows
