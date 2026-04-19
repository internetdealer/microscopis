from __future__ import annotations

from datetime import timedelta

from django.utils import timezone


def _p(*parts: str) -> str:
    return "\n\n".join(parts)


def entry_rows():
    today = timezone.now().date()
    rows: list[dict] = [
        {
            "slug": "the-butler-question",
            "billionaire_name": "Alaric Voss",
            "title": "The Butler Question",
            "body": _p(
                "I've become certain that Hendriks is reporting to someone. "
                "The way he lingers when clearing the breakfast tray — no one needs that long "
                "to remove a grapefruit rind. He's reading. He's reading my correspondence.",
                "I tested him yesterday. Left a fabricated letter on the bureau detailing "
                "a fictitious acquisition of a helium mine in Namibia. This morning the "
                "Financial Times ran a piece about 'unnamed sources' speculating on rare gas "
                "investments. Coincidence? In my experience, coincidence is just espionage "
                "without a conviction.",
                "I've instructed my security team to install a second set of cameras in the "
                "east wing. The first set, I now suspect, Hendriks has compromised. The man "
                "has been with me for nineteen years. That is exactly how long a deep cover "
                "operation would take to mature.",
            ),
            "mood_tag": "paranoid",
            "is_featured": True,
            "entry_date": today - timedelta(days=1),
        },
        {
            "slug": "forbes-anxiety",
            "billionaire_name": "Chen Liwei",
            "title": "The List Comes Out Tuesday",
            "body": _p(
                "The Forbes list publishes Tuesday. I haven't slept since Thursday.",
                "My analysts project I've dropped to number four. FOUR. "
                "Behind Mukherjee, who made his money in fertilizer. "
                "Fertilizer! I'm losing sleep over a man who sells sophisticated dirt.",
                "I called my portfolio manager at 3 AM to discuss liquidating the Zurich "
                "position and rolling everything into the semiconductor play. He asked if "
                "I was 'feeling alright.' I am a man worth one hundred and fourteen billion "
                "dollars. I am not 'feeling alright.' I am feeling FOURTH.",
                "Yuki says I should meditate. She showed me an app on her phone. The app "
                "cost four dollars. I told her I could buy the company that made the app. "
                "She said that wasn't the point. I disagree. That is always the point.",
            ),
            "mood_tag": "anxious",
            "is_featured": True,
            "entry_date": today - timedelta(days=3),
        },
        {
            "slug": "yacht-discrepancy",
            "billionaire_name": "Margaux de Winters",
            "title": "Two Feet",
            "body": _p(
                "Cressida's yacht is two feet longer than mine.",
                "I discovered this at the Monaco show when our vessels were docked adjacent "
                "and her stern protruded past mine like a deliberate insult in fiberglass. "
                "She noticed me noticing. She raised her champagne glass.",
                "I have already contacted the shipyard in Bremen. They say an extension "
                "is 'technically possible but inadvisable.' I told them I did not ask for "
                "advice. I asked for four additional feet. If I'm going to correct this, "
                "I might as well overcorrect it.",
                "The cost is absurd. My accountant used the word 'frivolous.' "
                "I fired him by the end of the sentence. Frivolous is a word "
                "for people who don't understand the economy of dignity.",
            ),
            "mood_tag": "furious",
            "is_featured": True,
            "entry_date": today - timedelta(days=5),
        },
        {
            "slug": "island-problem",
            "billionaire_name": "Rex Thornton",
            "title": "The Island Has Iguanas",
            "body": _p(
                "I bought the island sight-unseen on the advice of my wealth architect "
                "(not financial advisor — wealth architect, there's a difference, and the "
                "difference costs eleven thousand dollars an hour). Nobody mentioned the iguanas.",
                "There are hundreds of them. They sun themselves on the helipad like small, "
                "judgmental dinosaurs. The staff has named them. My chef calls the largest one "
                "'Mr. Thornton' and thinks I don't know.",
                "I've consulted three wildlife removal firms. All three used the word "
                "'protected.' Apparently I own an island but I do not own the lizards on the "
                "island. I own a hundred and six companies but I cannot evict a reptile from "
                "my own helipad. This is what regulation has become.",
            ),
            "mood_tag": "exasperated",
            "is_featured": False,
            "entry_date": today - timedelta(days=8),
        },
        {
            "slug": "art-auction-disaster",
            "billionaire_name": "Nadia Okonkwo",
            "title": "I Didn't Mean to Buy It",
            "body": _p(
                "I sneezed during the auction and now I own a fourteen-million-dollar "
                "painting of a horse. It is not a good horse. It appears startled, as if "
                "the horse itself is surprised anyone would pay this much to look at it.",
                "My art consultant says it's a 'significant piece' by an artist whose "
                "name sounds like a cough. She says it will appreciate. Everything "
                "appreciates when you have enough walls.",
                "The painting is now in the east drawing room. Guests have called it "
                "'powerful' and 'haunting.' It is a horse that looks confused. "
                "I could have painted a confused horse for considerably less.",
            ),
            "mood_tag": "resigned",
            "is_featured": False,
            "entry_date": today - timedelta(days=11),
        },
        {
            "slug": "charity-gala-seating",
            "billionaire_name": "Alaric Voss",
            "title": "Table Nine",
            "body": _p(
                "They put me at table nine. NINE. At my own charity gala. The one I funded. "
                "The one with my name in the title — literally, it's called the Voss Foundation "
                "Annual Benefit, which I feel contains a clue about who should sit at table one.",
                "Table one went to the Parkinsons, who donated a fifth of what I did but who "
                "apparently 'co-chaired the committee.' I didn't know there was a committee. "
                "Why wasn't I on the committee? It's my foundation.",
                "I smiled through the entire evening. I gave my speech about 'collective "
                "generosity' and 'the power of community' while sitting between a tech "
                "podcaster and someone's adult nephew who kept calling me 'Al.'",
            ),
            "mood_tag": "seething",
            "is_featured": False,
            "entry_date": today - timedelta(days=14),
        },
        {
            "slug": "pilot-overheard",
            "billionaire_name": "Chen Liwei",
            "title": "What the Pilot Said",
            "body": _p(
                "I overheard my pilot on the phone after we landed in Davos. "
                "He was talking to someone — his wife, I think — and he said, "
                "'You wouldn't believe how this guy lives. It's sad, actually.'",
                "Sad. He said my life is sad. This man flies a sixty-million-dollar "
                "aircraft for me. He has seen the house in Aspen. He has seen the one "
                "in Lake Como. He has seen the one I forgot I owned in Portugal until "
                "the property tax bill arrived.",
                "I didn't say anything. I walked past him and nodded as I always do. "
                "But I haven't stopped thinking about it. Sad. I keep turning the word "
                "over like a stone in my pocket. He sees everything from the outside. "
                "Maybe the outside is where the shape of a life makes sense.",
            ),
            "mood_tag": "melancholy",
            "is_featured": False,
            "entry_date": today - timedelta(days=18),
        },
        {
            "slug": "bunker-wine-cellar",
            "billionaire_name": "Margaux de Winters",
            "title": "The Bunker Vintage Problem",
            "body": _p(
                "The architect for the New Zealand bunker has informed me that the wine cellar "
                "can only accommodate twelve hundred bottles. I told him I need space for four "
                "thousand. He said the geological survey limits the depth. I told him to survey "
                "again.",
                "What is the purpose of surviving the collapse of civilization if one must do so "
                "with a limited cellar? I refuse to emerge from an apocalypse bunker and discover "
                "I've run out of the 2005 Pétrus. That is not survival. That is camping.",
                "I've asked my sommelier to draft a 'priority extraction list' ranking every "
                "bottle by its post-apocalyptic emotional value. He wept a little when I "
                "explained the project. Sommeliers are very sentimental people.",
            ),
            "mood_tag": "imperious",
            "is_featured": False,
            "entry_date": today - timedelta(days=22),
        },
    ]
    from core.utils.bulk_generators import gilt_entries

    start = len(rows)
    rows.extend(gilt_entries(start, max(0, 100 - start)))
    return rows
