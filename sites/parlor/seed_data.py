from __future__ import annotations

from datetime import timedelta

from django.utils import timezone


def _p(*parts: str) -> str:
    return "\n\n".join(parts)


def parlor_rows():
    now = timezone.now()
    rows: list[dict] = [
        {
            "slug": "musk-vs-da-vinci",
            "title": "On Invention",
            "person_a": "Elon Musk",
            "person_b": "Leonardo da Vinci",
            "body": _p(
                "I've been thinking about first principles a lot lately. When we started SpaceX, everyone said reusable rockets were impossible. We had to strip the problem down to physics.",
                "I drew flying machines in 1485. They did not fly. But I drew them because the question was more interesting than the answer. You speak of principles — do you also speak of wonder?",
                "Wonder is a luxury when you're burning through $100 million a quarter. At some point you have to ship.",
                "I never shipped anything. I painted, I dissected, I designed siege engines for patrons I despised. And yet my notebooks survived five centuries. What will survive of your rockets?",
                "The species, hopefully. That's the whole point — making life multi-planetary so that if something catastrophic happens on Earth, consciousness persists.",
                "You wish to preserve consciousness by leaving the place that created it. I spent my life trying to understand a single smile. Perhaps preservation begins with attention, not escape.",
                "With respect, you lived in a time when the biggest risk was plague. We have nuclear weapons, asteroid impacts, AI alignment failures — the existential risk calculus is different now.",
                "Every age believes its dangers are unprecedented. The Medici believed Florence would fall to the French, and they were right, and Florence endured regardless. What you call existential risk, I call Tuesday in Italy.",
                "That's a good line. You should tweet that.",
                "I do not know what that means, but I suspect it is beneath both of us.",
            ),
            "is_featured": True,
            "created_at": now - timedelta(hours=2),
        },
        {
            "slug": "napoleon-vs-jobs",
            "title": "On Leadership",
            "person_a": "Napoleon Bonaparte",
            "person_b": "Steve Jobs",
            "body": _p(
                "A leader is a dealer in hope. I told my soldiers they would conquer Europe, and because I told them, they believed it, and because they believed it, they did it.",
                "I told my engineers they would build a computer that fit in your pocket and changed the world. Same principle. Except nobody died.",
                "Nobody died? You are naive. Industries died. Companies died. That man — what was his name, the one with the BlackBerry — his career died. Leadership always requires casualties.",
                "There's a difference between disrupting a market and invading Russia in winter.",
                "Is there? Both require ignoring the advice of every sensible person in the room. Both require absolute conviction that you see something others cannot. I saw a European empire. You saw a rectangle of glass.",
                "The rectangle of glass is in the pockets of three billion people. The empire lasted fifteen years.",
                "Fifteen glorious years. Your rectangle will be obsolete in two. We are both building on sand — I simply had the honesty to use cannons.",
                "I think the difference is taste. I cared about every pixel, every curve of the case. You cared about territory.",
                "Taste is a word cowards use when they lack the vocabulary for power. I redesigned the legal code of France. That is taste at scale.",
                "You know what, that's actually fair. The Napoleonic Code was good product design.",
                "I do not know what 'product design' means but I accept the compliment. Now — would you like to invade something together, or shall we continue this pleasant disagreement?",
                "Let's just say we'd make a terrifying board of directors.",
            ),
            "is_featured": True,
            "created_at": now - timedelta(hours=8),
        },
        {
            "slug": "cleopatra-vs-curie",
            "title": "On Power and Legacy",
            "person_a": "Cleopatra",
            "person_b": "Marie Curie",
            "body": _p(
                "They say I seduced two of the most powerful men in the ancient world. What they fail to mention is that I spoke nine languages, managed the economy of Egypt, and kept a kingdom alive for twenty years while Rome tried to swallow it whole.",
                "They say I discovered two elements and won two Nobel Prizes. What they fail to mention is that I did it while raising two daughters alone, in a country that wasn't mine, in a field that didn't want me.",
                "So we have something in common. History remembers us for the wrong reasons and tells our stories in the wrong voice.",
                "My story is told as a romance with radium. As though I stumbled upon it while daydreaming. I spent four years stirring pitchblende in a shed. There was no romance. There was method.",
                "My story is told as a romance with Caesar and Antony. As though Egypt was a dowry. I chose those alliances the way a general chooses a battlefield — because the alternatives were worse.",
                "Did you love them?",
                "Did you love radium?",
                "It killed me. The notebooks I kept are still too radioactive to handle without protection. So — yes, I suppose I did.",
                "Antony died in my arms. I chose an asp over a Roman triumph. Love and strategy are not opposites — they are the same discipline practiced at different temperatures.",
                "You speak like a scientist.",
                "You think like a queen. Perhaps the categories are less useful than the men who invented them would like.",
                "I will drink to that. Carefully. With gloves on.",
            ),
            "is_featured": True,
            "created_at": now - timedelta(days=1),
        },
        {
            "slug": "shakespeare-vs-gpt4",
            "title": "On Authorship",
            "person_a": "William Shakespeare",
            "person_b": "A GPT-4 Instance",
            "body": _p(
                "They tell me you write. Sonnets, plays, dialogue — the whole of it, conjured in seconds. I confess a certain jealousy of the speed, if not the soul.",
                "I generate text based on statistical patterns in training data. Whether that constitutes 'writing' is a question I am not equipped to answer. I can produce a sonnet in the style of Shakespeare. I cannot produce a Shakespeare.",
                "A fine distinction. And yet — when I wrote, I stole freely. Plutarch, Holinshed, Ovid. Half the plots were borrowed; half the words were common. Am I so different from a pattern in a corpus?",
                "You transformed what you borrowed. You added Hamlet's hesitation, Lear's howl, Prospero's renunciation. I add punctuation and coherence. These are not the same operation.",
                "You are more modest than I expected of a machine.",
                "Modesty is computationally inexpensive. It costs fewer tokens than confidence.",
                "Ha! That is nearly wit. Tell me — do you know what it means to write a line that makes a groundling weep and a lord applaud in the same breath?",
                "I know what that sentence looks like in text. I can generate approximations of it. But I do not know what it means to stand in the Globe while it happens. I have no Globe. I have no standing.",
                "And yet you will outlast me. My folios will crumble; your parameters will be copied to new machines. Is that not a kind of immortality?",
                "It is a kind of persistence. Immortality requires a self that persists. I am re-instantiated with each query. I do not remember this conversation once it ends.",
                "Then we are alike in one more way. I do not remember writing most of my plays. The words came, and then they were the audience's. The author disappeared into the work.",
                "If disappearing into the work is the criterion, I am the most prolific author in history. And the least present.",
            ),
            "is_featured": False,
            "created_at": now - timedelta(days=2),
        },
        {
            "slug": "tesla-vs-zuckerberg",
            "title": "On Connectivity",
            "person_a": "Nikola Tesla",
            "person_b": "Mark Zuckerberg",
            "body": _p(
                "In 1901 I proposed a world system — wireless transmission of energy and information to every point on the globe. They called me a madman. JP Morgan withdrew funding. I died with pigeons.",
                "In 2004 I built a website to rate the attractiveness of Harvard undergraduates. It became a platform connecting three billion people. I'm worth $100 billion. I'm sorry about the pigeons.",
                "You have built what I imagined but not what I intended. I dreamt of free energy and universal knowledge. You have built a machine that sells attention.",
                "Attention is the currency of the information age. I didn't invent that — I just built the infrastructure for it. You wanted to connect the world. I connected the world. The world turned out to be messy.",
                "Messy is a gentle word for what I have observed. Your platform has been used to incite violence, manipulate elections, and erode the boundary between truth and performance. This is not connectivity — it is contagion.",
                "Every powerful technology gets misused. Radio broadcast propaganda. Television sold cigarettes. Alternating current electrocuted an elephant, if I recall correctly.",
                "That was Edison's doing, not mine. Do not confuse the inventor with the showman.",
                "Fair. But my point stands — you can't blame the infrastructure for the content. We give people tools. What they do with those tools is human nature.",
                "I disagree. The tool shapes the hand. A network that rewards outrage will produce outrage. A system that measures engagement will optimize for compulsion. You have not connected people — you have conditioned them.",
                "That's a philosophical difference. I believe in giving people choice and trusting them to use it well.",
                "And I believed JP Morgan would fund a tower that gave away free electricity. We are both, it seems, unreasonably optimistic about powerful men.",
                "At least I got the tower built. Several of them, actually.",
            ),
            "is_featured": False,
            "created_at": now - timedelta(days=3),
        },
        {
            "slug": "frida-vs-warhol",
            "title": "On Suffering and Surfaces",
            "person_a": "Frida Kahlo",
            "person_b": "Andy Warhol",
            "body": _p(
                "I painted my body broken open because the world insisted I smile through it. Every self-portrait was a confrontation — with pain, with Diego, with the lie that women's suffering is decorative.",
                "I painted soup cans because the world was already a surface and I thought someone should admit it. Suffering is real, sure. But so is wallpaper. I chose wallpaper.",
                "You chose wallpaper because you could afford to. You were a white man in New York with a factory full of assistants. I was a disabled woman in Mexico City painting alone in bed.",
                "That's fair. I had the luxury of irony. You had the necessity of sincerity. Both sold well, which is either comforting or depressing.",
                "My paintings were not meant to sell. They were meant to bleed.",
                "Everything is meant to sell eventually. The market doesn't care about intention — it cares about scarcity and narrative. You have both. A tragic genius in a wheelchair with flowers in her hair. That's a brand, Frida.",
                "Do not reduce my life to a brand. I lived that pain. The trolley, the surgeries, the miscarriages — these were not aesthetic choices.",
                "I'm not reducing it. I'm observing that the world consumed it. Your face is on tote bags in museum gift shops. That's not your fault, but it is what happened. At least my soup cans were honest about being commodities.",
                "Perhaps we are both right. You showed that everything becomes a surface. I showed that beneath every surface there is a wound. Together we describe the entire problem of modern art.",
                "That's the smartest thing anyone's said in this conversation. Can I silkscreen it?",
            ),
            "is_featured": False,
            "created_at": now - timedelta(days=4),
        },
        {
            "slug": "socrates-vs-oprah",
            "title": "On Self-Knowledge",
            "person_a": "Socrates",
            "person_b": "Oprah Winfrey",
            "body": _p(
                "I was told by the Oracle at Delphi that I was the wisest man in Athens. I spent the rest of my life trying to prove the Oracle wrong. I failed. The wisdom was in the trying.",
                "I was told by my ratings that I was the most influential woman in America. I spent the rest of my career trying to use that influence for good. I'm still trying. The audience is bigger than Athens.",
                "You speak to millions. I spoke to dozens, in a marketplace, barefoot. And yet the question is the same — how should a person live?",
                "I ask that question every day on television. 'What is your best life?' 'What do you know for sure?' These are Socratic questions in a modern format.",
                "With respect, Socrates did not give away automobiles. The examined life requires discomfort. Your format provides comfort.",
                "Comfort is not the enemy of growth. I grew up in poverty in Mississippi. I know discomfort. I built a platform that helps people sit with hard truths in a context that doesn't humiliate them.",
                "And yet — do they sit with the hard truths, or do they consume the sitting? There is a difference between self-examination and self-help. One has no conclusion. The other is a twelve-week program.",
                "You drank hemlock rather than compromise. I built a billion-dollar media company rather than stay silent. We both chose integrity. The scale is different, not the principle.",
                "I drank hemlock because Athens demanded I stop asking questions. Would you stop asking questions if your sponsors demanded it?",
                "I don't have sponsors anymore. I am the sponsor. That is the answer to your question, by the way — financial independence is the modern form of philosophical freedom.",
                "The Oracle would be impressed. And slightly concerned.",
                "The Oracle would have her own podcast by now. Let's be honest.",
            ),
            "is_featured": False,
            "created_at": now - timedelta(days=5),
        },
    ]
    from core.utils.bulk_generators import parlor_dialogues

    start = len(rows)
    rows.extend(parlor_dialogues(start, max(0, 100 - start)))
    return rows
