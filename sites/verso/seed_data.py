"""
Default VERSO categories and articles (AI, agents, human/AI). Used by ``seed_verso``.

Themes reflect widely discussed 2025–2026 trends: agentic systems, tool use,
multi-agent orchestration, reasoning models, governance, and human–AI collaboration.
"""

from __future__ import annotations

CATEGORIES: list[dict] = [
    {
        "slug": "ai",
        "name": "AI",
        "description": (
            "Foundation models, reasoning, safety, and alignment—how large language "
            "systems are built, deployed, and governed."
        ),
        "sort_order": 0,
    },
    {
        "slug": "agents",
        "name": "Agents",
        "description": (
            "Autonomous and semi-autonomous systems that plan, call tools, and "
            "coordinate workflows beyond single-turn chat."
        ),
        "sort_order": 1,
    },
    {
        "slug": "human",
        "name": "Human",
        "description": (
            "Judgment, creativity, labor, and responsibility where people meet "
            "machine inference—AI versus human, and everything in between."
        ),
        "sort_order": 2,
    },
]


def _p(*parts: str) -> str:
    return "\n\n".join(parts)


ARTICLES: list[dict] = [
    {
        "slug": "the-agentic-turn",
        "category": "agents",
        "title": "The Agentic Turn: When the Model Stops Answering and Starts Doing",
        "excerpt": (
            "The industry’s center of gravity is shifting from chat interfaces to systems "
            "that pursue goals, invoke tools, and revise plans when reality disagrees."
        ),
        "author": "Nina Okonkwo",
        "published_at": "2026-03-28",
        "read_minutes": 9,
        "is_featured": True,
        "image_url": "https://images.unsplash.com/photo-1485827404703-89b55fcc565e?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "For years, the dominant metaphor for large language models was a brilliant "
            "interlocutor: you ask, it answers, you decide what happens next. That framing "
            "still matters for drafting and brainstorming. But production systems are "
            "increasingly built around a different pattern—one closer to an assistant who "
            "can open files, run commands, file tickets, and come back with a status update.",
            "This shift is often called agentic AI: the model is wrapped in a loop that "
            "observes outcomes, selects actions, and iterates. Tool APIs (function calling), "
            "retrieval, and memory turn a static completion into something that behaves more "
            "like software with agency—bounded, fallible agency, but agency nonetheless.",
            "The engineering tradeoffs are familiar from any complex automation: reliability, "
            "timeouts, cost ceilings, and clear escalation paths when the agent drifts. What "
            "is new is how cheaply natural-language reasoning can sit at the center of that "
            "stack, routing between specialized steps that used to require bespoke code.",
            "None of this dissolves the need for human judgment at the edges. It relocates "
            "it—from typing the next prompt to designing the loop, auditing traces, and "
            "deciding which objectives are safe to hand off. The agentic turn is not the "
            "end of oversight; it is a change in where oversight must attach.",
        ),
    },
    {
        "slug": "alignment-in-the-loop",
        "category": "ai",
        "title": "Alignment Is Not a Feature, It Is a Relationship",
        "excerpt": (
            "Safety work is sometimes treated as a checklist bolted onto a model. In "
            "practice, alignment is negotiated continuously between builders, deployers, and users."
        ),
        "author": "Marcus Webb",
        "published_at": "2026-03-27",
        "read_minutes": 10,
        "is_featured": True,
        "image_url": "https://images.unsplash.com/photo-1589829547916-f8f697b19b16?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "Public discussion of “AI safety” often imagines a one-time fix: train once, "
            "red-team once, ship. Real deployments are messier. Models are updated, prompts "
            "mutate, integrations change, and adversaries adapt. Alignment is less a sealed "
            "property of weights than an ongoing relationship between a system and the "
            "environment it touches.",
            "That is why governance layers—usage policies, monitoring, rate limits, human "
            "review for sensitive actions—sit alongside technical mitigations. They are not "
            "a substitute for sound training; they are the membrane through which models meet "
            "institutions that cannot afford silent failure.",
            "Reasoning-oriented architectures complicate the picture in a productive way. "
            "Longer chains of thought create more surface area for intervention: you can "
            "inspect traces, require citations for tool calls, or halt when confidence "
            "metrics cross thresholds. The question is whether organizations invest in those "
            "hooks or treat models as opaque oracles.",
            "Readers and citizens do not need to pick sides between optimism and panic. They "
            "need clarity about who is accountable when a model-enabled workflow causes harm, "
            "and which incentives reward careful deployment over speed. Alignment, in that "
            "sense, is as much a political and organizational problem as a technical one.",
        ),
    },
    {
        "slug": "judgment-beyond-the-score",
        "category": "human",
        "title": "Judgment Beyond the Score: Where Humans Still Matter",
        "excerpt": (
            "Models can rank, summarize, and simulate fluently. The hard part remains knowing "
            "when fluency is misleading—and who bears responsibility when it is."
        ),
        "author": "Elena Voss",
        "published_at": "2026-03-26",
        "read_minutes": 8,
        "is_featured": True,
        "image_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "Machine learning has always excelled at pattern recognition at scale. Large "
            "language models add something seductive: they can narrate those patterns in "
            "convincing prose. That combination is powerful for triage and exploration—and "
            "dangerous when mistaken for authoritative judgment in domains where stakes are "
            "personal, legal, or existential.",
            "Human expertise is not merely slower inference. It includes standing commitments: "
            "professional ethics, liability, institutional memory, and the willingness to "
            "say “I don’t know” when data are thin. Models optimize for plausible continuation "
            "of text; people (ideally) optimize for defensible decisions under uncertainty.",
            "The productive synthesis is not “replace the expert” or “ignore the model.” It "
            "is to separate tasks where statistical correlation suffices from tasks where "
            "accountability must be traceable to a person or a role. That separation is "
            "organizational design, not a slider in a settings panel.",
            "As tools improve, the scarcest resource may become the discernment to know when "
            "to trust automation—and the courage to refuse it when the cost of error is "
            "asymmetric. That discernment is human work, even when machines do most of the typing.",
        ),
    },
    {
        "slug": "orchestrating-many-minds",
        "category": "agents",
        "title": "Orchestrating Many Minds: Multi-Agent Systems and the Division of Labor",
        "excerpt": (
            "Single-agent demos are easy to film. Durable systems often split roles—research, "
            "critique, synthesis—across multiple models and tools."
        ),
        "author": "James Liu",
        "published_at": "2026-03-25",
        "read_minutes": 11,
        "is_featured": False,
        "image_url": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "When a task decomposes cleanly—fetch data, check constraints, draft a report—"
            "multi-agent patterns mirror how teams already work. One component might focus "
            "on retrieval, another on verification, a third on style and consistency. The "
            "orchestration layer decides sequencing, retries, and handoffs.",
            "Frameworks and platforms differ, but the architectural idea is stable: reduce "
            "each agent’s scope so failures are localized, and make interfaces between agents "
            "explicit. Without that discipline, you recreate a monolith with extra latency.",
            "The cost profile changes. More calls and more context mean budgets matter sooner. "
            "Production teams reach for caching, smaller specialist models, and asynchronous "
            "queues—less glamorous than a demo, more representative of real deployments.",
            "The open research question is not whether multi-agent systems can look impressive "
            "on benchmarks, but whether they can be operated with the same rigor as other "
            "mission-critical software: observability, rollback, and post-incident review.",
        ),
    },
    {
        "slug": "reasoning-and-the-stack",
        "category": "ai",
        "title": "Reasoning Models and the Stack They Demand",
        "excerpt": (
            "Longer inference chains unlock harder tasks—and new failure modes. The surrounding "
            "infrastructure has to catch up."
        ),
        "author": "Sofia Hernandez",
        "published_at": "2026-03-24",
        "read_minutes": 7,
        "is_featured": False,
        "image_url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "Reasoning-focused models—those encouraged to expose intermediate steps—change "
            "the user experience from a single burst of text to something closer to a trace. "
            "That trace can be audited, which is invaluable for debugging and compliance. It "
            "can also be long, which stresses latency budgets and logging pipelines.",
            "Downstream systems must store and search traces, redact secrets, and correlate "
            "them with business identifiers. The model is only one layer in a stack that "
            "includes eval harnesses, evaluators for evaluators, and runtime guardrails.",
            "Open-weight alternatives continue to narrow the gap for teams that need on-prem "
            "or air-gapped deployments. The tradeoff is operational burden: someone has to "
            "own upgrades, quantization choices, and incident response without vendor defaults.",
            "None of this diminishes the research frontier; it grounds it. Reasoning is not "
            "magic—it is computation arranged so mistakes can be seen before they ship.",
        ),
    },
    {
        "slug": "augmentation-displacement-drift",
        "category": "human",
        "title": "Augmentation, Displacement, or Drift: Work After the Model",
        "excerpt": (
            "The debate over “AI taking jobs” often flattens a messier reality: roles will "
            "combine, vanish, and emerge in the same organization within a single year."
        ),
        "author": "David Chen",
        "published_at": "2026-03-23",
        "read_minutes": 10,
        "is_featured": False,
        "image_url": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "Historical automation rarely deletes a job title overnight. It changes task "
            "mixes: fewer hours on rote steps, more on exception handling, client interface, "
            "or system supervision. Language models accelerate that reshuffling for knowledge "
            "work because they touch communication, coding, and analysis simultaneously.",
            "Augmentation stories are easy to tell when tools raise median quality. Displacement "
            "stories appear when employers redefine roles around throughput. Drift is quieter: "
            "workloads shift toward verifying machine output—an activity that may not show up "
            "in headcount but shows up in burnout.",
            "Policy responses—training, collective bargaining, procurement rules—lag technical "
            "change. That gap matters because the distributional effects of AI are not uniform "
            "across regions, industries, or seniority levels.",
            "VERSO’s interest here is not predicting a single future. It is insisting that "
            "“AI vs human” is the wrong frame when the real question is which humans get "
            "leverage, which get surveillance, and who sets the defaults.",
        ),
    },
    # --- Additional essays (agents / AI / human vs machine), published April 2026 ---
    {
        "slug": "permission-boundary-agents",
        "category": "agents",
        "title": "The Permission Boundary: What Your Agent Is Allowed to Touch",
        "excerpt": (
            "An agent without scoped permissions is a liability. Drawing the boundary—files, "
            "APIs, spend—is where product, security, and governance actually meet."
        ),
        "author": "Nina Okonkwo",
        "published_at": "2026-04-10",
        "read_minutes": 9,
        "is_featured": True,
        "image_url": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "The demo shows an agent booking travel and updating a spreadsheet. Production "
            "asks uglier questions: which identities may it assume, which secrets can it read, "
            "and what happens when it loops on a failing tool call with your corporate card attached?",
            "Permission design is not a one-time ACL list. It is a product decision about "
            "trust gradients—read-only exploration versus write access, sandboxed browsers "
            "versus live CRM updates, automatic retries versus human approval for irreversible steps.",
            "Security teams rightly worry about prompt injection crossing those boundaries; "
            "operators worry about silent partial failures that look like success in a trace. "
            "The durable pattern is least privilege plus explicit escalation paths: narrow defaults, "
            "loud failures, and humans who can revoke scope without redeploying the model.",
            "Agents will spread where boundaries are legible. The organizations that win will "
            "treat permissioning as a first-class surface—versioned, audited, and boring—"
            "not as an afterthought bolted on after the demo wins the budget.",
        ),
    },
    {
        "slug": "inference-economics",
        "category": "ai",
        "title": "Inference Economics: Who Pays When Every Click Is a Model Call",
        "excerpt": (
            "Latency and quality are not the only constraints. As models sit behind every "
            "feature, unit economics and metering become product strategy."
        ),
        "author": "Marcus Webb",
        "published_at": "2026-04-09",
        "read_minutes": 8,
        "is_featured": True,
        "image_url": "https://images.unsplash.com/photo-1611974789855-9c2a0a4756a8?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "Training costs dominate headlines, but inference costs dominate spreadsheets. "
            "Every autocomplete, summarization, and reranking step is a billable sequence of "
            "tokens—often multiplied by retrieval, tool calls, and retries in agentic flows.",
            "That shifts how products are priced and how teams choose model sizes. Smaller "
            "models with caching and routing beat raw capability when the alternative is "
            "unbounded spend on long contexts in high-traffic surfaces.",
            "Customers rarely see the meter; they see latency and quality. Finance sees the "
            "margin. The tension between product ambition and unit economics is where “AI "
            "for everyone” either becomes sustainable infrastructure or a subsidized loss leader.",
            "Transparency about inference cost—internally and, where appropriate, externally—"
            "is not pessimism. It is a prerequisite for honest roadmaps and for avoiding the "
            "trap of shipping features that cannot survive their own success.",
        ),
    },
    {
        "slug": "man-machine-myth-total-war",
        "category": "human",
        "title": "Man, Machine, and the Myth of Total War",
        "excerpt": (
            "The ‘war’ between humans and computers is a catchy headline. The reality is "
            "competition, codependence, and a fight over who sets the rules."
        ),
        "author": "Elena Voss",
        "published_at": "2026-04-08",
        "read_minutes": 9,
        "is_featured": True,
        "image_url": "https://images.unsplash.com/photo-1531746797551-88f8194d4c1d?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "Pop narratives frame the present as a zero-sum contest: humans versus machines, "
            "with a winner-take-all finish line. History suggests something else—waves of "
            "automation that reshuffle tasks while leaving institutions, power, and accountability "
            "stubbornly human.",
            "What does look like conflict is the fight over speed, data, and defaults. Who "
            "can deploy first? Whose model is embedded in which workflow? Which errors are "
            "tolerated as the cost of scale? Those are political and economic battles, not "
            "a species-level duel in a sci-fi trailer.",
            "Computers excel at scale and speed; humans still carry liability, ethics, and "
            "the messy work of saying no when metrics look good but reality does not. The "
            "danger is not that machines ‘win’—it is that we outsource judgment to interfaces "
            "we do not understand and cannot challenge.",
            "A more useful framing than war is stewardship: who owns the feedback loop, who "
            "audits the trace, and who pays when the system fails someone who had no seat at "
            "the design table. That is where humans and machines are genuinely entangled.",
        ),
    },
    {
        "slug": "hardening-agent-pipelines",
        "category": "agents",
        "title": "Hardening Agent Pipelines: Retries, Sandboxes, and Kill Switches",
        "excerpt": (
            "The difference between a demo and production is what happens on the third "
            "failure, not the first success."
        ),
        "author": "James Liu",
        "published_at": "2026-04-07",
        "read_minutes": 10,
        "is_featured": False,
        "image_url": "https://images.unsplash.com/photo-1563013544-824ae1b704d3?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "Reliability engineering did not disappear because the planner is a language model. "
            "Timeouts, exponential backoff, circuit breakers, and idempotent operations—"
            "these remain the grammar of systems that survive contact with the real world.",
            "Sandboxes matter when agents execute code or browse: isolate filesystems, "
            "network egress, and secret injection so a single bad prompt cannot become a "
            "lateral movement story. Kill switches matter when cost or risk spirals: "
            "hard caps on spend, token ceilings, and human-in-the-loop gates for irreversible actions.",
            "Observability is not optional. Structured traces, correlation IDs, and redaction "
            "pipelines are how you debug production agents without turning every incident into "
            "forensics-by-screenshot.",
            "The teams that ship durable agents are often the ones who sound boring on "
            "purpose: they rehearse failure modes, measure recovery time, and treat ‘happy path’ "
            "demos as marketing, not architecture.",
        ),
    },
    {
        "slug": "synthetic-media-provenance",
        "category": "ai",
        "title": "Synthetic Media and the Arms Race for Provenance",
        "excerpt": (
            "As generation becomes trivial, the scarce resource becomes trust: knowing what "
            "was made, by whom, and under what constraints."
        ),
        "author": "Sofia Hernandez",
        "published_at": "2026-04-06",
        "read_minutes": 8,
        "is_featured": False,
        "image_url": "https://images.unsplash.com/photo-1639322537228-f710d846310a?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "Text, image, audio, and video synthesis are no longer laboratory experiments. "
            "They are consumer features. That shifts the problem from ‘can we generate?’ to "
            "‘can we attribute, verify, and revoke?’—questions that touch cryptography, law, "
            "and platform design at once.",
            "Provenance proposals—metadata, watermarking, signing pipelines—compete with "
            "adversaries who optimize for evasion. There is no single technical fix; there "
            "is a layered stack of signals, each imperfect in isolation, sometimes useful together.",
            "Institutions that need defensible records—newsrooms, courts, enterprises—"
            "cannot rely on vibe alone. They need workflows: capture chains, editorial review, "
            "and explicit policies for when synthetic assistance is disclosed.",
            "The ‘war’ between authentic and synthetic is less about banning tools than about "
            "raising the cost of deception and protecting the reputational channels that still "
            "matter when pixels lie fluently.",
        ),
    },
    {
        "slug": "cognitive-offloading-price",
        "category": "human",
        "title": "Cognitive Offloading: The Hidden Price of Letting Machines Decide",
        "excerpt": (
            "Delegation feels efficient until judgment atrophies. The risk is not laziness; "
            "it is unrecoverable loss of institutional memory."
        ),
        "author": "David Chen",
        "published_at": "2026-04-05",
        "read_minutes": 9,
        "is_featured": False,
        "image_url": "https://images.unsplash.com/photo-1532619675608-729875fa83e7?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "When a model drafts, summarizes, and routes, humans stop rehearsing the full "
            "chain of reasoning. That saves time. It also means fewer people know how to "
            "reconstruct the answer when the tool is wrong—or unavailable.",
            "Organizations may wake up with a competence cliff: senior staff who trust "
            "outputs they no longer verify, and juniors who never learned the underlying craft. "
            "That is not inevitable; it is a training and governance design problem.",
            "Cognitive offloading is not unique to AI; calculators and spell-checkers did it "
            "first. The difference is scale and authority: systems that sit at the center of "
            "decision pipelines can reshape norms faster than any prior assistive tech.",
            "The healthy middle is selective automation: keep humans in the loop where "
            "accountability is real, invest in drills without the tool, and treat models as "
            "amplifiers of expertise rather than replacements for it.",
        ),
    },
    {
        "slug": "sub-agents-conflict",
        "category": "agents",
        "title": "When Sub-Agents Conflict: Orchestration as Diplomacy",
        "excerpt": (
            "Multiple specialized agents can outperform one monolith—if they agree on facts, "
            "interfaces, and who gets the final word."
        ),
        "author": "Alexandra Reed",
        "published_at": "2026-04-04",
        "read_minutes": 7,
        "is_featured": False,
        "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "Splitting work across sub-agents—research, critique, synthesis—mirrors "
            "human teams. It also introduces coordination failures: duplicated effort, "
            "contradictory conclusions, and ambiguous ownership of the final output.",
            "Orchestration layers need explicit contracts: shared schemas for facts, "
            "deterministic tie-breakers, and escalation paths when confidence diverges. "
            "Without that, you get impressive parallelism with a fragile merge step.",
            "Some designs use debate or arbitration: a third agent reviews conflict, or a "
            "human adjudicates. The point is not novelty; it is reducing variance in outcomes "
            "when the system is under load.",
            "Treat multi-agent systems as distributed systems with natural-language interfaces. "
            "The failure modes are familiar; the remediation is engineering discipline, not "
            "bigger prompts alone.",
        ),
    },
    {
        "slug": "frontier-labs-concentration",
        "category": "ai",
        "title": "Frontier Labs and the Concentration of Capability",
        "excerpt": (
            "The cutting edge of general models remains expensive and concentrated. That "
            "shapes access, safety norms, and who gets to define ‘default’ behavior."
        ),
        "author": "Marcus Webb",
        "published_at": "2026-04-03",
        "read_minutes": 8,
        "is_featured": False,
        "image_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "Foundation models cluster where capital, talent, and compute concentrate. "
            "Open-weight ecosystems broaden deployment, but the frontier of capability "
            "often follows a handful of well-funded labs and their partners.",
            "That concentration matters for policy. Default safety behaviors, cultural "
            "biases, and update cadence are shaped by a small set of teams—often under "
            "commercial pressure and public scrutiny at once.",
            "Decentralization is not a slogan; it is a research and infrastructure agenda: "
            "competition law, open tooling, public datasets, and regional capacity so that "
            "‘AI’ is not synonymous with a single geography or stack.",
            "Readers should not confuse capability with wisdom. The most powerful models "
            "are tools; the institutions that deploy them still decide what counts as a good outcome.",
        ),
    },
    {
        "slug": "creativity-automation-taste",
        "category": "human",
        "title": "Creativity After Automation: Human Taste as the Scarce Input",
        "excerpt": (
            "When machines generate endless variants, the bottleneck is no longer output—"
            "it is selection, framing, and the courage to say this is finished."
        ),
        "author": "Sofia Hernandez",
        "published_at": "2026-04-02",
        "read_minutes": 8,
        "is_featured": False,
        "image_url": "https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=1600&q=80",
        "image_credit": "Photo via Unsplash",
        "body": _p(
            "Generative tools flood the zone with drafts, palettes, and hooks. Abundance "
            "does not erase the creative act; it moves it toward curation—knowing what to "
            "keep, what to cut, and what story the work is supposed to tell.",
            "Taste is not a mystical gift; it is trained judgment, accumulated across "
            "failure and feedback. The risk is that organizations skip that training and "
            "ship volume instead of voice.",
            "In competition between humans and machines, the unfair advantage for people "
            "may be narrow but decisive: accountability, biography, and stakes that "
            "cannot be simulated from averages.",
            "The creative industries that thrive will treat models as instruments in an "
            "ensemble—fast sketchers, tireless editors—but they will still pay for directors "
            "who know when to stop generating and start committing.",
        ),
    },
]
