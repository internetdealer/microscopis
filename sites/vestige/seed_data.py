"""Seed rows for ``VestigeExhibit`` — things the internet forgot."""

from __future__ import annotations

from datetime import timedelta

from django.utils import timezone


def _p(*parts: str) -> str:
    return "\n\n".join(parts)


def exhibit_rows():
    now = timezone.now()
    rows: list[dict] = [
        {
            "slug": "the-dancing-baby",
            "title": "The Dancing Baby (Baby Cha-Cha)",
            "exhibit_type": "meme",
            "era_desc": "1996–1998",
            "body": _p(
                "Before memes had a name, there was a 3D-rendered baby doing the cha-cha. The "
                "animation was created by Ron Lussier using Character Studio software and was "
                "never intended for distribution — it was a demo file, a proof of concept for "
                "motion-capture technology. Someone emailed it to a friend. That friend emailed "
                "it to everyone. By 1997, the Dancing Baby had been forwarded to more inboxes "
                "than any piece of media in history, on connections that took four minutes to "
                "download a three-second clip.",
                "It appeared on Ally McBeal. It was referenced in news broadcasts. It became "
                "the first piece of internet culture to cross into mainstream awareness, which "
                "meant it was also the first to be declared 'dead' by the people who found it "
                "first. The lifecycle that would later define every meme — creation, spread, "
                "mainstream adoption, ironic reuse, oblivion — was established here, in 1996, "
                "by a low-polygon infant with no face.",
                "The Dancing Baby is the fossil record of viral culture. It proved that the "
                "internet could create shared references without gatekeepers, that a joke could "
                "become universal without anyone deciding it should. It also proved the corollary: "
                "that universality is a death sentence. The moment everyone knows the joke, the "
                "joke is over. The baby still dances in the archives, but no one is watching.",
            ),
            "last_seen": "Occasionally resurrected in nostalgic threads, always briefly",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Dancing_baby",
            "wayback_url": "",
            "is_featured": True,
            "curated_at": now - timedelta(hours=3),
        },
        {
            "slug": "geocities-neighborhoods",
            "title": "GeoCities Neighborhoods",
            "exhibit_type": "site",
            "era_desc": "1994–2009",
            "body": _p(
                "GeoCities organized the internet into neighborhoods. Your personal website "
                "lived on a virtual street in a virtual city: Hollywood for entertainment, "
                "SiliconValley for tech, Heartland for family pages, Area51 for the weird stuff "
                "that didn't fit anywhere else. It was a metaphor so literal it was almost "
                "embarrassing, and it worked perfectly because the internet was new enough that "
                "people needed a metaphor.",
                "Each page was a monument to individual taste unfiltered by algorithms or design "
                "standards. Animated GIFs of flames. Visitor counters. Guestbooks where strangers "
                "left messages like 'Cool page!' and meant it. MIDI files that auto-played when "
                "you loaded the page — always the same three songs: the X-Files theme, 'Stairway "
                "to Heaven,' or the Mortal Kombat soundtrack. The pages were ugly and sincere and "
                "they represented something we didn't know we'd lose: the idea that a website "
                "could be a place.",
                "Yahoo acquired GeoCities in 1999 for $3.57 billion and shut it down in 2009 "
                "after deciding it wasn't profitable enough. The Archive Team scrambled to save "
                "what they could. They preserved about a terabyte — millions of pages, billions "
                "of words, countless animated 'Under Construction' signs. But what they couldn't "
                "save was the feeling: the frontier optimism of a time when having a web page "
                "was an act of identity, not an obligation.",
            ),
            "last_seen": "oocities.org mirror; Archive Team torrents",
            "wikipedia_url": "https://en.wikipedia.org/wiki/GeoCities",
            "wayback_url": "https://web.archive.org/web/2009/http://www.geocities.com/",
            "is_featured": True,
            "curated_at": now - timedelta(hours=10),
        },
        {
            "slug": "the-hamster-dance",
            "title": "The Hamster Dance",
            "exhibit_type": "trend",
            "era_desc": "1998–2000",
            "body": _p(
                "A Canadian art student named Deidre LaCarte made a webpage of animated hamster "
                "GIFs as a competition with her friend to see who could generate the most web "
                "traffic. The page had no content — just rows of tiny hamsters dancing to a "
                "sped-up sample of Roger Miller's 'Whistle Stop,' which most people recognized "
                "as 'that song from Robin Hood.' It was the stupidest thing on the internet, "
                "which at the time was a competitive field.",
                "By August 1999, the page was getting 60,000 visits a day. The Hamster Dance "
                "spawned a music single that charted in Canada and several European countries. "
                "There was merchandise. There was a sequel site. There was a brief, surreal "
                "period where a corporate meeting could be derailed by someone saying 'Have you "
                "seen the hamster thing?' and everyone would nod solemnly.",
                "What made the Hamster Dance significant was its pointlessness. It had no "
                "message, no creator agenda, no monetization strategy. It existed because "
                "someone made it and other people liked it and that was the entire economy. "
                "The modern internet — optimized, algorithmic, relentlessly purposeful — could "
                "not produce a Hamster Dance. It requires a kind of ambient creativity that "
                "only thrives in the absence of metrics.",
            ),
            "last_seen": "hamsterdance.org redirects to a mobile game; original GIFs lost",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Hampster_Dance",
            "wayback_url": "https://web.archive.org/web/1999/http://www.hamsterdance.com/",
            "is_featured": True,
            "curated_at": now - timedelta(days=1),
        },
        {
            "slug": "google-wave",
            "title": "Google Wave",
            "exhibit_type": "project",
            "era_desc": "2009–2010",
            "body": _p(
                "Google Wave was going to replace email. That was the pitch at Google I/O 2009, "
                "delivered in an eighty-minute demo that received a standing ovation from an "
                "audience that had just watched real-time collaborative editing happen inside "
                "a threaded conversation for the first time. The product was email, chat, wiki, "
                "and document collaboration fused into a single protocol. It was the future. "
                "It lasted fourteen months.",
                "The problem wasn't the technology — it was the metaphor, or the lack of one. "
                "People didn't know what a 'wave' was. Was it a conversation? A document? A "
                "project space? Google's answer was 'yes, all of those,' which is another way "
                "of saying 'we don't know either.' Users received invitations, opened Wave, "
                "stared at an empty screen, typed 'Hello?' to no one, and closed the tab.",
                "Every feature Google Wave invented was eventually adopted by other products. "
                "Slack has threaded conversations. Google Docs has real-time collaboration. "
                "Notion has the kitchen-sink-workspace concept. Wave was right about everything "
                "except timing. It showed up ten years early, with no tutorial and no clear "
                "purpose, and it died the way prophets die: correct, ignored, and eventually "
                "plagiarized.",
            ),
            "last_seen": "Apache Wave (open-source continuation), archived 2018",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Apache_Wave",
            "wayback_url": "",
            "is_featured": False,
            "curated_at": now - timedelta(days=2),
        },
        {
            "slug": "lonelygirl15",
            "title": "lonelygirl15",
            "exhibit_type": "person",
            "era_desc": "2006–2008",
            "body": _p(
                "Bree was a sixteen-year-old girl who posted video diaries to YouTube from her "
                "bedroom. She talked about her strict religious parents, her crush on a boy named "
                "Daniel, her struggles with loneliness. The videos were intimate and artless and "
                "they accumulated millions of views because the internet in 2006 was still small "
                "enough that a single authentic voice could become the main character.",
                "Then the New York Times revealed that Bree was an actress named Jessica Rose, "
                "the videos were scripted by a team of filmmakers, and the entire thing was an "
                "elaborate narrative fiction — the first YouTube-native series. The revelation "
                "caused a crisis that seems quaint now: people felt betrayed by a fictional "
                "character. The line between 'content' and 'reality' had been crossed for the "
                "first time on a platform that didn't know the line existed.",
                "lonelygirl15 ran for three seasons and spawned spin-offs, but its real legacy "
                "is the template it created. Every curated Instagram life, every 'authentic' "
                "vlog with professional lighting, every parasocial relationship between creator "
                "and audience — it all started with a fake girl in a fake bedroom telling fake "
                "stories to real people who wanted to believe.",
            ),
            "last_seen": "YouTube channel still exists; last upload 2008; 100M+ total views",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Lonelygirl15",
            "wayback_url": "",
            "is_featured": False,
            "curated_at": now - timedelta(days=3),
        },
        {
            "slug": "the-million-dollar-homepage",
            "title": "The Million Dollar Homepage",
            "exhibit_type": "site",
            "era_desc": "2005–2006",
            "body": _p(
                "A 21-year-old British student named Alex Tew needed tuition money. His idea: "
                "a webpage with exactly one million pixels, sold at one dollar per pixel to "
                "advertisers. Minimum purchase: a 10×10 block. The page would stay up forever. "
                "It was the dumbest business plan imaginable and it raised exactly one million "
                "dollars in five months.",
                "The page became a time capsule of mid-2000s internet commerce. Tiny logos "
                "for online casinos, poker sites, ringtone providers, and the occasional "
                "legitimate business are frozen in a grid that looks like a fever dream of "
                "capitalism. Most of the links are dead now. The casinos closed. The poker "
                "sites were banned. The ringtone economy collapsed when smartphones arrived. "
                "The pixels remain, pointing to domains that no longer exist.",
                "What made the Million Dollar Homepage remarkable was that it worked once and "
                "could never work again. Thousands of imitators launched similar pages — the "
                "million euro homepage, the million pixel page, the million whatever page — "
                "and none of them made money because the entire value proposition was novelty. "
                "The first person to sell pixels was a genius. The second was a footnote.",
            ),
            "last_seen": "milliondollarhomepage.com — still live, most links dead",
            "wikipedia_url": "https://en.wikipedia.org/wiki/The_Million_Dollar_Homepage",
            "wayback_url": "https://web.archive.org/web/2006/http://www.milliondollarhomepage.com/",
            "is_featured": False,
            "curated_at": now - timedelta(days=4),
        },
        {
            "slug": "webring-culture",
            "title": "Webrings",
            "exhibit_type": "trend",
            "era_desc": "1995–2003",
            "body": _p(
                "Before Google made finding things easy, webrings made finding things communal. "
                "A webring was exactly what it sounded like: a circular chain of websites linked "
                "together by topic. You'd visit a page about model trains, click 'Next' in the "
                "webring navigation bar, and arrive at another page about model trains, maintained "
                "by a different person in a different country who shared your specific, narrow "
                "enthusiasm.",
                "The experience was browsing in the original sense — not searching, not scrolling, "
                "but wandering through a curated neighborhood of strangers who cared about the "
                "same thing you did. Each click was a small act of trust: you didn't know where "
                "you'd end up, but you knew it would be relevant because a human had decided it "
                "belonged. The algorithm was a person. The recommendation engine was taste.",
                "Webrings died because search engines made them unnecessary and social media made "
                "them structurally impossible. You can't form a ring when all traffic flows "
                "through a central platform. The internet stopped being a network of places and "
                "became a network of feeds, and feeds don't have a 'Next' button because they "
                "never end. The webring was the internet's last navigational metaphor that "
                "assumed you might want to leave.",
            ),
            "last_seen": "A few hobbyist webrings still operate; most maintained ironically",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Webring",
            "wayback_url": "",
            "is_featured": False,
            "curated_at": now - timedelta(days=6),
        },
        {
            "slug": "ask-jeeves",
            "title": "Ask Jeeves",
            "exhibit_type": "site",
            "era_desc": "1996–2006",
            "body": _p(
                "Before Google taught the world to type keywords, Ask Jeeves invited you to "
                "ask a question in plain English. The butler mascot — dignified, bowler-hatted, "
                "impossibly patient — suggested that the internet was a concierge service. You "
                "could type 'Where is the nearest pizza place?' and Jeeves would try to understand.",
                "He usually didn't. The natural language processing of the late 1990s was "
                "ambitious and terrible in roughly equal measure. But the premise was ahead "
                "of its time: twenty years later, every AI assistant does what Jeeves promised. "
                "The difference is that Jeeves admitted he was guessing.",
                "Ask Jeeves became Ask.com in 2006, dropped the butler, and tried to compete "
                "with Google on Google's terms. It lost. The lesson: when you have a mascot "
                "that people remember fondly, don't fire him. The internet has never been short "
                "of search engines. It has always been short of butlers.",
            ),
            "last_seen": "ask.com still exists; Jeeves appears in occasional marketing nostalgia",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Ask.com",
            "wayback_url": "https://web.archive.org/web/2005/http://www.ask.com/",
            "is_featured": False,
            "curated_at": now - timedelta(days=7),
        },
        {
            "slug": "vine-six-seconds",
            "title": "Vine",
            "exhibit_type": "project",
            "era_desc": "2013–2017",
            "body": _p(
                "Six seconds. That was the constraint, and it turned out to be the magic. Vine "
                "proved that creativity thrives under restriction: in six seconds you could tell "
                "a joke, demonstrate a talent, or create a tiny surrealist film. The format was "
                "too short for pretension and too long for nothing.",
                "Vine created a generation of creators who went on to dominate YouTube, TikTok, "
                "and Hollywood. King Bach, Lele Pons, the 'why you always lying' guy — all Vine "
                "products. The platform was a comedy farm system, incubating talent that other "
                "platforms would harvest.",
                "Twitter acquired Vine and killed it in January 2017, reportedly because it "
                "couldn't figure out how to make money from it. The archive was preserved but "
                "the community wasn't — and communities, unlike files, cannot be backed up.",
            ),
            "last_seen": "Vine archive preserved; spiritual successor: TikTok",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Vine_(service)",
            "wayback_url": "",
            "is_featured": False,
            "curated_at": now - timedelta(days=8),
        },
        {
            "slug": "stumbleupon",
            "title": "StumbleUpon",
            "exhibit_type": "site",
            "era_desc": "2001–2018",
            "body": _p(
                "StumbleUpon was a serendipity engine. You clicked a button and it showed you "
                "a random interesting webpage. That was the entire product. In an internet "
                "increasingly organized by search and social algorithms, StumbleUpon offered "
                "something radical: the experience of being pleasantly surprised by something "
                "you didn't know existed.",
                "The magic was in the recommendation algorithm, which learned your tastes and "
                "served pages that were relevant enough to be interesting but different enough "
                "to be unexpected. It was the closest the internet ever came to the experience "
                "of browsing a bookstore.",
                "StumbleUpon shut down in 2018 and was replaced by Mix, which nobody used. The "
                "internet lost its best tool for accidental discovery, and we've been trapped "
                "in filter bubbles ever since.",
            ),
            "last_seen": "Rebranded as Mix (2018), which also shut down",
            "wikipedia_url": "https://en.wikipedia.org/wiki/StumbleUpon",
            "wayback_url": "https://web.archive.org/web/2012/http://www.stumbleupon.com/",
            "is_featured": False,
            "curated_at": now - timedelta(days=9),
        },
        {
            "slug": "aol-instant-messenger",
            "title": "AIM (AOL Instant Messenger)",
            "exhibit_type": "project",
            "era_desc": "1997–2017",
            "body": _p(
                "The buddy list. The away message. The door-opening sound. AIM was the social "
                "network before social networks existed — a real-time text communication system "
                "that organized an entire generation's social life around a sidebar of screen "
                "names and status indicators.",
                "Away messages became an art form: passive-aggressive lyrics, cryptic quotes, "
                "and elaborate ASCII art that said 'I am at dinner' in the most dramatic way "
                "possible. Your screen name was your first act of online identity, chosen at "
                "age 13 and regretted by 15.",
                "AIM shut down on December 15, 2017. By then, messaging had migrated to phones, "
                "and the concept of being 'online' had become meaningless because everyone was "
                "always online. AIM belonged to an era when logging on was an event — a threshold "
                "you crossed from the offline world into a digital one. That threshold no longer "
                "exists, which is either progress or loss depending on your age.",
            ),
            "last_seen": "Shut down December 2017; no successor; everyone uses everything",
            "wikipedia_url": "https://en.wikipedia.org/wiki/AIM_(software)",
            "wayback_url": "",
            "is_featured": False,
            "curated_at": now - timedelta(days=10),
        },
        {
            "slug": "clippy-office-assistant",
            "title": "Clippy (Office Assistant)",
            "exhibit_type": "meme",
            "era_desc": "1997–2004",
            "body": _p(
                "'It looks like you're writing a letter. Would you like help?' No. The answer "
                "was always no. Clippy — Microsoft's animated paperclip assistant — was the "
                "most hated UI element in software history and, retroactively, the most beloved. "
                "He was annoying when he existed and missed when he left.",
                "Clippy represented Microsoft's first attempt at an AI assistant: context-aware, "
                "proactive, and catastrophically bad at reading the room. He would appear during "
                "your most focused moments to suggest help you didn't need, like a waiter "
                "interrupting a proposal to ask about dessert.",
                "Microsoft removed Clippy in Office 2007. Two decades later, AI assistants are "
                "everywhere, doing exactly what Clippy tried to do — anticipating user needs and "
                "offering unsolicited help. The difference is that modern assistants are slightly "
                "better at timing. Clippy was right about the future; he was just too early and "
                "too enthusiastic.",
            ),
            "last_seen": "Resurrected as Microsoft Teams emoji in 2021; meme status: immortal",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Office_Assistant",
            "wayback_url": "",
            "is_featured": False,
            "curated_at": now - timedelta(days=11),
        },
        {
            "slug": "newgrounds-flash",
            "title": "Newgrounds",
            "exhibit_type": "site",
            "era_desc": "1995–present",
            "body": _p(
                "Newgrounds was the YouTube of Flash animation — a portal where anyone could "
                "upload interactive games, cartoons, and music. It launched careers (the creators "
                "of Super Meat Boy, Castle Crashers, and Alien Hominid all started here) and "
                "defined an entire aesthetic: crude, funny, violent, and deeply sincere.",
                "The site was also a democracy. Users rated everything, and the portal system "
                "surfaced the best content through community voting rather than algorithms. "
                "Quality was uneven — most submissions were terrible — but the system produced "
                "gems with a reliability that modern recommendation engines struggle to match.",
                "When Adobe killed Flash in 2020, it nearly killed Newgrounds. The site survived "
                "by migrating to HTML5, but the Flash era was irreplaceable: a time when making "
                "interactive internet art was accessible to anyone with a pirated copy of Flash "
                "MX and an afternoon free.",
            ),
            "last_seen": "Still active; HTML5 migration complete; preserving Flash archive via Ruffle",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Newgrounds",
            "wayback_url": "https://web.archive.org/web/2004/http://www.newgrounds.com/",
            "is_featured": False,
            "curated_at": now - timedelta(days=12),
        },
        {
            "slug": "all-your-base",
            "title": "All Your Base Are Belong to Us",
            "exhibit_type": "meme",
            "era_desc": "2000–2002",
            "body": _p(
                "In the opening cutscene of the 1989 Sega Genesis game Zero Wing, a poorly "
                "translated villain declares: 'All your base are belong to us.' The line was "
                "absurd, ungrammatical, and impossible to forget. In 2001, someone set it to "
                "music and Photoshopped it onto every image imaginable. It became the first "
                "internet-native meme to achieve cultural escape velocity.",
                "'All Your Base' was important because it established the template for viral "
                "remix culture: take one element, apply it to everything, share endlessly. "
                "The joke wasn't the line itself — it was the act of finding new surfaces to "
                "put it on. Billboards, road signs, the Eiffel Tower. The meme was the format.",
                "By 2002 it was over. The meme's rapid lifecycle — discovery, saturation, "
                "death — became the model for everything that followed. Every meme since "
                "has followed the same arc, just faster.",
            ),
            "last_seen": "Referenced in Ready Player One; appears in retro meme compilations",
            "wikipedia_url": "https://en.wikipedia.org/wiki/All_your_base_are_belong_to_us",
            "wayback_url": "",
            "is_featured": False,
            "curated_at": now - timedelta(days=13),
        },
        {
            "slug": "netscape-navigator",
            "title": "Netscape Navigator",
            "exhibit_type": "project",
            "era_desc": "1994–2008",
            "body": _p(
                "Netscape Navigator made the World Wide Web usable for ordinary people. Before "
                "Netscape, the web was a research project. After Netscape, it was a medium. The "
                "browser's 1994 launch turned the internet from a curiosity into a revolution "
                "and kicked off the dot-com boom.",
                "Then Microsoft bundled Internet Explorer with Windows, and the browser wars "
                "began. Netscape lost — slowly, then all at once. By 2003, IE controlled 95% "
                "of the browser market. Netscape open-sourced its code as Mozilla, which "
                "eventually became Firefox, which kept the flame alive until Chrome ate everything.",
                "Netscape Navigator was the browser that proved the internet was for everyone. "
                "Its death at the hands of bundling and monopoly power is a story about what "
                "happens when a transformative technology meets an incumbent with distribution "
                "advantages. The internet remembers Netscape the way democracies remember "
                "founders: imperfect, essential, and impossible to un-invent.",
            ),
            "last_seen": "Mozilla Firefox carries the lineage; Netscape brand last used 2008",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Netscape_Navigator",
            "wayback_url": "https://web.archive.org/web/1999/http://www.netscape.com/",
            "is_featured": False,
            "curated_at": now - timedelta(days=14),
        },
        {
            "slug": "blink-tag",
            "title": "The Blink Tag",
            "exhibit_type": "trend",
            "era_desc": "1994–2013",
            "body": _p(
                "The <blink> tag made text flash on and off. That was its only function, and it "
                "was the most annoying thing in the history of web development. Netscape engineer "
                "Lou Montulli reportedly invented it as a joke during a bar conversation. It "
                "shipped anyway. The internet embraced it with the enthusiasm of a child who "
                "has been given a drum.",
                "Every personal webpage in the late 1990s had at least one blinking element, "
                "usually 'UNDER CONSTRUCTION' or 'WELCOME TO MY PAGE.' It was universally "
                "hated by designers and universally loved by people making their first webpage. "
                "The blink tag was democratic: it gave everyone the power to be annoying.",
                "Browsers quietly dropped support between 2009 and 2013. No one mourned. But "
                "the blink tag's legacy is philosophical: it proved that the web would be shaped "
                "by what users wanted to do, not what designers thought they should do. And what "
                "users wanted, overwhelmingly, was to make things flash.",
            ),
            "last_seen": "CSS animation: blink keeps the spirit alive for those who seek it",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Blink_element",
            "wayback_url": "",
            "is_featured": False,
            "curated_at": now - timedelta(days=15),
        },
        {
            "slug": "hit-counters",
            "title": "Hit Counters",
            "exhibit_type": "trend",
            "era_desc": "1996–2005",
            "body": _p(
                "'You are visitor #000437.' The hit counter was the first metric of the web "
                "— a tiny odometer at the bottom of every personal page that tracked how many "
                "people had visited. It was usually wrong, easily gamed, and profoundly "
                "meaningful to the person who installed it.",
                "Hit counters came in hundreds of styles: plain text, 3D digits, slot machine "
                "animations, digital clock fonts. Choosing your counter style was a design "
                "decision on par with choosing your page's background MIDI. The counter said "
                "'people come here, and I count them, and that matters.'",
                "Google Analytics killed the hit counter by making traffic data private and "
                "sophisticated. We gained precision and lost transparency. A hit counter was a "
                "public confession of vanity — 'I care how many people see this' — and the "
                "modern internet, which cares about metrics more than anything, hides them "
                "behind dashboards that only the owner can see. We got better data and worse "
                "honesty.",
            ),
            "last_seen": "Ironic use on retro-styled pages; free counter services mostly dead",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Web_counter",
            "wayback_url": "",
            "is_featured": False,
            "curated_at": now - timedelta(days=16),
        },
    ]
    from core.utils.bulk_generators import vestige_exhibits

    start = len(rows)
    rows.extend(vestige_exhibits(start, max(0, 100 - start)))
    return rows
