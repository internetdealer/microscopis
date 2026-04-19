"""Seed rows for ``ResidueFragment`` — real dead websites and their digital remains."""

from __future__ import annotations

from datetime import timedelta

from django.utils import timezone


def _p(*parts: str) -> str:
    return "\n\n".join(parts)


def fragment_rows():
    now = timezone.now()
    rows: list[dict] = [
        {
            "slug": "geocities-the-lost-suburbs",
            "original_url": "http://www.geocities.com/",
            "fragment_type": "page",
            "site_name": "GeoCities",
            "wayback_url": "https://web.archive.org/web/2009/http://www.geocities.com/",
            "recovered_text": _p(
                "GeoCities was the third-most-visited site on the entire web in the late 1990s. "
                "Yahoo acquired it in 1999 for $3.57 billion, then quietly shut it down on "
                "October 26, 2009. With it vanished an estimated 38 million user-built pages — "
                "personal shrines, fan fiction archives, amateur astronomy logs, recipe "
                "collections, devotional pages for pets, tributes to deceased relatives. An "
                "entire stratum of early web culture, organized into whimsical "
                "'neighborhoods' like SunsetStrip, SiliconValley, and Heartland.",
                "The Archive Team scrambled to save what they could before the shutdown, "
                "recovering roughly 1.2 terabytes of pages. But millions were lost — pages "
                "built by people who never imagined a corporation would one day flip a switch "
                "and erase their work. GeoCities was messy, garish, full of auto-playing MIDIs "
                "and tiled backgrounds and broken visitor counters. It was also the first place "
                "most people ever published anything on the internet. Nothing that replaced it "
                "ever gave ordinary people quite the same sense of ownership over their tiny "
                "corner of the web.",
                "What died with GeoCities was not just data. It was proof that millions of "
                "people, given a blank page and no audience, will build something anyway.",
            ),
            "context_notes": "Yahoo gave users a few months' warning. The Archive Team's torrent of the recovered data remains one of the largest web preservation efforts ever attempted.",
            "is_featured": True,
            "archived_at": now - timedelta(hours=2),
        },
        {
            "slug": "friendster-the-first-network",
            "original_url": "http://www.friendster.com/",
            "fragment_type": "profile",
            "site_name": "Friendster",
            "wayback_url": "https://web.archive.org/web/2011/http://www.friendster.com/",
            "recovered_text": _p(
                "Friendster launched in 2002, a full year before MySpace and two years before "
                "Facebook. It was the first social network to reach mainstream adoption, the "
                "site that taught a generation the mechanics of online friendship — profile "
                "photos, testimonials, networks of connections. At its peak it had over 115 "
                "million registered users, particularly dominant in Southeast Asia.",
                "The site buckled under its own success. Servers couldn't handle the load, "
                "pages took 40 seconds to render, and management made a series of hostile "
                "decisions — deleting 'Fakesters' (fictional profiles that users loved), "
                "refusing to sell to Google for $30 million. By 2009 it had pivoted to a "
                "gaming platform. In 2015 it shut down entirely, and in the process deleted "
                "all user photos, messages, and profile data without warning.",
                "The Friendster diaspora seeded every social network that followed. Its failure "
                "became a case study in how not to scale, and its ghost haunts every platform "
                "that takes its users' content for granted.",
            ),
            "context_notes": "Friendster's patent portfolio was sold to Facebook in 2010. The domain was later acquired by a Malaysian payments company.",
            "is_featured": True,
            "archived_at": now - timedelta(hours=6),
        },
        {
            "slug": "google-plus-the-ghost-town",
            "original_url": "https://plus.google.com/",
            "fragment_type": "page",
            "site_name": "Google+",
            "wayback_url": "https://web.archive.org/web/2018/https://plus.google.com/",
            "recovered_text": _p(
                "Google+ launched in June 2011 as Google's answer to Facebook. The company "
                "forced integration across its entire product line — you needed a Google+ "
                "account to comment on YouTube, rate apps on the Play Store, or even use some "
                "Gmail features. At one point Google claimed 300 million 'active' users, a "
                "figure widely mocked since most of that activity was involuntary.",
                "Behind the coerced engagement numbers lay a genuine community of photographers, "
                "tech enthusiasts, and writers who appreciated its Circles feature and long-form "
                "post format. They were a minority, but a devoted one. Google shut down the "
                "consumer version on April 2, 2019, citing a data breach that exposed the "
                "private profile data of up to 500,000 users — a breach Google had known about "
                "for months and chosen not to disclose.",
                "Users were given a window to export their data via Google Takeout. Many didn't. "
                "Years of posts, photos, and comment threads vanished. Google+ became shorthand "
                "for a particular kind of corporate failure: a product nobody asked for, forced "
                "on everyone, then killed when it became inconvenient.",
            ),
            "context_notes": "Google+ was the pet project of Vic Gundotra. After his departure in 2014, the platform was effectively orphaned inside Google.",
            "is_featured": True,
            "archived_at": now - timedelta(hours=12),
        },
        {
            "slug": "vine-six-seconds-of-culture",
            "original_url": "https://vine.co/",
            "fragment_type": "page",
            "site_name": "Vine",
            "wayback_url": "https://web.archive.org/web/2016/https://vine.co/",
            "recovered_text": _p(
                "Vine launched in January 2013: a platform for six-second looping videos. The "
                "constraint was the point. Within that tiny window, creators invented new forms "
                "of comedy, music, and visual storytelling. It birthed catchphrases that entered "
                "mainstream culture, launched careers (Lele Pons, King Bach, Shawn Mendes), "
                "and proved that brevity could be an art form rather than a limitation.",
                "Twitter, which had acquired Vine before launch for $30 million, never figured "
                "out how to monetize it. By 2016 the top creators were defecting to YouTube "
                "and Instagram, which offered actual revenue sharing. Twitter announced Vine's "
                "closure in October 2016; the app stopped accepting new posts on January 17, "
                "2017. The archive remained viewable until the domain was converted to a "
                "stripped-down Vine Camera app, then finally dissolved.",
                "A community-driven archive at vine.co preserved millions of clips. But the "
                "creative ecosystem — the remix culture, the duets, the comedy chains built "
                "across hundreds of accounts — was irretrievable. TikTok owes its entire "
                "grammar to Vine, but the original text is gone.",
            ),
            "context_notes": "Twitter reportedly turned down an acquisition offer from Facebook for Vine. The platform had 200 million active monthly viewers at its peak.",
            "is_featured": False,
            "archived_at": now - timedelta(days=1),
        },
        {
            "slug": "digg-v4-the-redesign-that-killed",
            "original_url": "http://digg.com/",
            "fragment_type": "page",
            "site_name": "Digg v4",
            "wayback_url": "https://web.archive.org/web/2010/http://digg.com/",
            "recovered_text": _p(
                "Digg was once the front page of the internet — the place where links went "
                "viral before 'viral' was a word people used for websites. At its peak in 2008 "
                "it commanded 236 million unique visitors and turned down a $200 million "
                "acquisition offer from Google. Then, on August 25, 2010, Digg launched its v4 "
                "redesign and destroyed itself virtually overnight.",
                "The redesign stripped users of their ability to bury stories, gave publishers "
                "direct submission power (effectively selling the front page to corporations), "
                "and erased years of user history. The community revolted. In the most symbolic "
                "act of digital protest imaginable, Digg's own front page filled with links to "
                "Reddit — users deliberately upvoting their competitor as a farewell gesture. "
                "Traffic cratered by 26% in a single month.",
                "In 2012, what remained of Digg was sold to Betaworks for $500,000 — one "
                "quarter of one percent of the price Google once offered. The Digg v4 collapse "
                "became the canonical example of how a single bad product decision can kill a "
                "platform that took years to build.",
            ),
            "context_notes": "The 'Digg exodus' of August 2010 is widely credited with Reddit's rise to mainstream dominance. Kevin Rose, Digg's founder, later joined Google Ventures.",
            "is_featured": False,
            "archived_at": now - timedelta(days=2),
        },
        {
            "slug": "delicious-bookmarks-lost",
            "original_url": "http://del.icio.us/",
            "fragment_type": "listing",
            "site_name": "del.icio.us",
            "wayback_url": "https://web.archive.org/web/2008/http://del.icio.us/",
            "recovered_text": _p(
                "del.icio.us — later Delicious — was the pioneer of social bookmarking. "
                "Founded by Joshua Schachter in 2003, it introduced the concept of tagging to "
                "the mainstream web. Users saved and categorized links with free-form tags, "
                "creating a folksonomy — a taxonomy built from below, by actual people "
                "describing what they found interesting in their own words.",
                "Yahoo acquired Delicious in 2005 and promptly neglected it. A leaked internal "
                "slide in 2010 listed it under 'sunset,' triggering a user panic and mass data "
                "exports. It was sold to AVOS Systems in 2011, which rebuilt it from scratch "
                "and managed to lose most of the legacy bookmark data in the migration. "
                "Subsequent owners — Science Inc., then Pinboard's Maciej Ceglowski — tried "
                "to preserve what was left.",
                "At its height, Delicious held hundreds of millions of bookmarks — a collective "
                "map of what the internet's most curious users thought was worth saving. The "
                "irony of a bookmarking service failing to preserve its own data remains one "
                "of the web's bitterest jokes.",
            ),
            "context_notes": "Joshua Schachter originally built del.icio.us to manage his own collection of 20,000 bookmarks. The site's tag cloud feature became one of the defining UI patterns of Web 2.0.",
            "is_featured": False,
            "archived_at": now - timedelta(days=3),
        },
        {
            "slug": "myspace-the-great-data-loss",
            "original_url": "http://www.myspace.com/",
            "fragment_type": "profile",
            "site_name": "MySpace",
            "wayback_url": "https://web.archive.org/web/2008/http://www.myspace.com/",
            "recovered_text": _p(
                "Before Facebook, there was MySpace — and before the sanitized feeds of modern "
                "social media, there was the glorious chaos of a MySpace profile. Users had "
                "full control over their page's HTML and CSS, which meant every profile was a "
                "unique collision of auto-playing songs, glitter GIFs, custom cursors, and "
                "color schemes that would make a designer weep. Tom was everyone's first friend.",
                "In 2013, MySpace relaunched with a sleek new design by Justin Timberlake's "
                "team. To make it work, they migrated to new servers — and in the process, "
                "quietly lost approximately 50 million songs uploaded by 14 million artists "
                "between 2003 and 2015. Photos, blog posts, and videos from the same era "
                "were also destroyed. MySpace blamed a faulty server migration.",
                "For an entire generation of independent musicians, MySpace was their first and "
                "sometimes only distribution platform. Demos, live recordings, bedroom EPs that "
                "existed nowhere else — gone. The MySpace data loss is the largest destruction "
                "of music in the internet era, and it happened not with a bang but with a "
                "corporate shrug.",
            ),
            "context_notes": "In 2019, MySpace confirmed that all content uploaded before 2016 was unrecoverable. The Internet Archive preserved some profiles, but the embedded media was largely lost.",
            "is_featured": False,
            "archived_at": now - timedelta(days=5),
        },
        {
            "slug": "google-reader-rss-dies",
            "original_url": "http://www.google.com/reader/",
            "fragment_type": "page",
            "site_name": "Google Reader",
            "wayback_url": "https://web.archive.org/web/2013/http://www.google.com/reader/",
            "recovered_text": _p(
                "Google Reader was an RSS aggregator that launched in 2005 and became the "
                "nervous system of the independent web. Bloggers, journalists, researchers, "
                "and curious readers used it to follow hundreds of sources without relying on "
                "any algorithm to decide what they should see. You subscribed. It showed you "
                "everything. The simplicity was the point.",
                "Google shut it down on July 1, 2013, citing declining usage — a decline Google "
                "itself had engineered by removing social features, neglecting the interface, "
                "and pushing users toward Google+. The announcement triggered more public outcry "
                "than almost any product shutdown in tech history. A Change.org petition "
                "gathered over 100,000 signatures in days.",
                "The death of Google Reader didn't just kill a product. It accelerated the death "
                "of RSS as a mainstream technology, which in turn accelerated the centralization "
                "of the web around algorithmic feeds controlled by a handful of platforms. Many "
                "of the information ecosystem problems we live with now trace a direct line "
                "back to that July afternoon when Google decided that open syndication wasn't "
                "worth maintaining.",
            ),
            "context_notes": "Former Google Reader product manager confirmed that internal politics, not user numbers, drove the shutdown. Feedly and Inoreader absorbed most refugees but never matched Reader's market share.",
            "is_featured": False,
            "archived_at": now - timedelta(days=7),
        },
        {
            "slug": "posterous-acqui-hired-to-death",
            "original_url": "http://posterous.com/",
            "fragment_type": "post",
            "site_name": "Posterous",
            "wayback_url": "https://web.archive.org/web/2012/http://posterous.com/",
            "recovered_text": _p(
                "Posterous launched in 2008 with a radical promise: you could create a blog "
                "post by sending an email. No login, no dashboard, no configuration — just "
                "write and send. It was blogging stripped to its barest essence, and it worked "
                "beautifully. The platform attracted writers, photographers, and casual sharers "
                "who wanted to publish without friction.",
                "Twitter acquired Posterous in March 2012. Within a year, Twitter announced the "
                "platform would shut down on April 30, 2013. Users were given a tool to export "
                "their data, but the tool was buggy and the timeline was short. Many users "
                "discovered the shutdown only after it happened. Years of posts — personal "
                "essays, family photo albums, travel journals — evaporated.",
                "Posterous became the textbook example of an 'acqui-hire' — a startup bought "
                "not for its product or users, but for its engineering team. The product and "
                "its community were treated as acceptable collateral damage. The Posterous team "
                "went on to build things at Twitter. What their users had built was simply "
                "thrown away.",
            ),
            "context_notes": "Posterous co-founder Sachin Agarwal later publicly expressed regret about how the shutdown was handled. The platform had hosted over 15 million blogs at its peak.",
            "is_featured": False,
            "archived_at": now - timedelta(days=10),
        },
        {
            "slug": "megaupload-seized-by-fbi",
            "original_url": "http://www.megaupload.com/",
            "fragment_type": "page",
            "site_name": "Megaupload",
            "wayback_url": "https://web.archive.org/web/2011/http://www.megaupload.com/",
            "recovered_text": _p(
                "On January 19, 2012, the FBI seized Megaupload's servers and shut down the "
                "site as part of a massive criminal indictment against founder Kim Dotcom. At "
                "the time, Megaupload accounted for 4% of all internet traffic worldwide. The "
                "DOJ called it 'the largest criminal copyright case in history.' The site's "
                "landing page was replaced with an FBI seizure notice that became one of the "
                "most iconic images of internet enforcement.",
                "The shutdown was legally and ethically tangled. Yes, Megaupload hosted vast "
                "quantities of pirated content. But it also hosted legitimate files — business "
                "documents, personal backups, independent media, academic datasets. When the "
                "servers were seized, millions of legitimate users lost access to their data "
                "with no recourse. The hosting company, Carpathia, held the data for months "
                "hoping for a legal resolution, then began deleting it.",
                "The Megaupload case raised questions that remain unresolved: who is responsible "
                "when a platform is destroyed and legal users' data goes with it? The criminal "
                "case against Kim Dotcom dragged on for over a decade. The files are long gone.",
            ),
            "context_notes": "At seizure, Megaupload had 180 million registered users and 50 million daily visitors. Kim Dotcom launched a successor, Mega, in 2013.",
            "is_featured": False,
            "archived_at": now - timedelta(days=14),
        },
    ]
    from core.utils.bulk_generators import residue_fragments

    start = len(rows)
    rows.extend(residue_fragments(start, max(0, 100 - start)))
    return rows
