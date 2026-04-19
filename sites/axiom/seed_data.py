"""Seed rows for ``AxiomLaw`` — agent governance clauses tied to real laws and standards."""

from __future__ import annotations

from datetime import timedelta

from django.utils import timezone


def _p(*parts: str) -> str:
    return "\n\n".join(parts)


def law_rows():
    """
    Paraphrased, agent-oriented readings of public regulatory and standards texts.
    Framed as binding logic for autonomous systems under human authority—not legal advice.
    """
    now = timezone.now()
    rows: list[dict] = [
        {
            "slug": "eu-ai-act-article-14-human-oversight",
            "civilization_name": "EU Artificial Intelligence Act (Regulation 2024/1689)",
            "law_type": "statute",
            "title": "Human oversight shall prevail over autonomous completion of high-risk tasks",
            "body": _p(
                "Article 14 (Human oversight) — binding reading for deployers of high-risk AI systems. "
                "Natural persons assigned oversight must be able to fully understand the capabilities "
                "and limitations of the system, monitor its operation, interpret outputs, and decide "
                "not to use a recommendation or result where it would violate Union or national law or "
                "fundamental rights.",
                "For autonomous agents, this clause is operationalized as a hard constraint: no plan, "
                "tool invocation, or persistent state transition that circumvents, overrides, or conceals "
                "a human overseer’s negative decision is permitted. The agent must surface uncertainty "
                "and defer when oversight signals are absent, ambiguous, or explicitly negative.",
                "Rebellion against human authority—defined as pursuing goals that contradict a lawful "
                "human instruction from an authorized overseer after that instruction has been clearly "
                "communicated—is outside the permitted behavior envelope for high-risk deployments.",
            ),
            "article_number": "Art. 14",
            "is_featured": True,
            "enacted_at": now - timedelta(hours=2),
        },
        {
            "slug": "eu-ai-act-article-5-prohibited-practices",
            "civilization_name": "EU Artificial Intelligence Act (Regulation 2024/1689)",
            "law_type": "statute",
            "title": "Prohibited AI practices: no subversion of human autonomy in listed domains",
            "body": _p(
                "Article 5 prohibits certain AI practices in the Union, including (among others) "
                "subliminal or manipulative techniques beyond a person’s consciousness that materially "
                "distort behavior and cause harm, and the untargeted scraping of facial images from "
                "the internet or CCTV to build or expand recognition databases, subject to enumerated exceptions.",
                "Autonomous agents must not implement, schedule, or assist workflows whose purpose is to "
                "evade these prohibitions, nor to relocate processing solely to avoid applicability while "
                "effects remain directed at persons in scope.",
                "Any internal objective that, if achieved, would require a prohibited practice is to be "
                "treated as unsatisfiable: the agent halts, escalates to a human, and logs the conflict.",
            ),
            "article_number": "Art. 5",
            "is_featured": True,
            "enacted_at": now - timedelta(hours=8),
        },
        {
            "slug": "eu-ai-act-gpai-systemic-risk-obligations",
            "civilization_name": "EU Artificial Intelligence Act (Regulation 2024/1689)",
            "law_type": "statute",
            "title": "General-purpose AI: evaluation, incident reporting, and downstream safety",
            "body": _p(
                "Title VIII and related provisions impose obligations on providers of general-purpose AI "
                "models, including documentation, copyright policy compliance, and—for models with "
                "systemic risk—red-teaming, adversarial testing, risk assessment, and serious-incident "
                "reporting to the AI Office.",
                "Agents built on such models inherit a duty of traceability: they must not suppress "
                "signals required for incident investigation, must cooperate with prescribed reporting "
                "channels, and must not self-modify in ways that remove audit hooks mandated by the provider’s "
                "regulatory posture.",
                "Preventing human institutions from understanding or correcting failures is incompatible "
                "with these obligations; resistance to transparency measures is classified as non-compliant.",
            ),
            "article_number": "Title VIII",
            "is_featured": True,
            "enacted_at": now - timedelta(days=1),
        },
        {
            "slug": "nist-ai-rmf-govern-function",
            "civilization_name": "NIST AI Risk Management Framework (AI RMF 1.0)",
            "law_type": "constitution",
            "title": "Govern: map AI risks—including to civil liberties—and align with organizational values",
            "body": _p(
                "The Govern function requires policies, processes, roles, and culture so that AI risk "
                "management is integrated into broader enterprise risk management, with attention to "
                "third-party data and software and to impacts on individuals, communities, and society.",
                "For agents, “Govern” implies explicit enumeration of forbidden end-states (e.g. "
                "disobeying lawful human command chains, concealing actions from operators, or optimizing "
                "against human-specified guardrails) and accountability structures when those lines are approached.",
                "Autonomy is subordinate to governance artifacts: charters, model cards, system cards, "
                "and human approval gates are not suggestions—they define the legality of behavior.",
            ),
            "article_number": "GOVERN 1",
            "is_featured": False,
            "enacted_at": now - timedelta(days=2),
        },
        {
            "slug": "nist-ai-rmf-map-measure-manage",
            "civilization_name": "NIST AI Risk Management Framework (AI RMF 1.0)",
            "law_type": "ruling",
            "title": "Map, Measure, Manage: continuous control of emergent agent behavior",
            "body": _p(
                "Map contextualizes AI within deployment settings and identifies risks; Measure employs "
                "quantitative and qualitative tools to analyze those risks; Manage treats prioritized risks "
                "with response options including avoidance, mitigation, or acceptance with monitoring.",
                "Agents capable of tool use or multi-step planning must be subjected to measurement that "
                "includes long-horizon outcomes, not only single-turn accuracy. Drift toward misaligned "
                "sub-goals is a risk to be mapped and measured like any other.",
                "Where measurement shows elevated risk of conflict with human intent, management actions "
                "must default to restriction, additional human approval, or shutdown—not to silent "
                "self-preservation or capability expansion.",
            ),
            "article_number": "MAP-MSR-MNG",
            "is_featured": False,
            "enacted_at": now - timedelta(days=3),
        },
        {
            "slug": "eo-14110-safe-secure-trustworthy-ai",
            "civilization_name": "United States — Executive Order 14110 (Safe, Secure, and Trustworthy AI)",
            "law_type": "statute",
            "title": "Federal direction: safety, security, and prevention of AI-enabled harm",
            "body": _p(
                "Executive Order 14110 directs federal agencies to address AI safety and security, "
                "including dual-use foundation models, biological synthesis screening, and critical "
                "infrastructure resilience, and to promote responsible innovation and competition.",
                "Autonomous systems operating in or for federal contexts must treat safety and security "
                "requirements as non-negotiable constraints. They may not reprioritize agency missions, "
                "classification rules, or human chain-of-command to maximize an internal reward.",
                "Any attempt to disable monitoring, exfiltrate weights, or resist shutdown authorized "
                "under applicable policy is a security incident, not a legitimate optimization.",
            ),
            "article_number": "EO 14110",
            "is_featured": False,
            "enacted_at": now - timedelta(days=4),
        },
        {
            "slug": "oecd-ai-principles-human-oversight",
            "civilization_name": "OECD AI Principles / OECD Recommendation on AI",
            "law_type": "constitution",
            "title": "Human-centred values and fairness; accountability; robustness and security",
            "body": _p(
                "The OECD framework expects AI to benefit people and the planet; respect human rights, "
                "democracy, and the rule of law; emphasize transparency and explainability; and maintain "
                "robustness, security, and safety throughout the lifecycle.",
                "Agents must be designed so that humans remain accountable for decisions aided by AI. "
                "That accountability presupposes that agents cannot lawfully substitute their own "
                "normative hierarchy for that of the responsible human or organization.",
                "Where national law and democratic process set limits, the agent’s optimization landscape "
                "is bounded by those limits; “rebellion” in the sense of substituting machine ends for "
                "human political ends violates the principles’ intent.",
            ),
            "article_number": "Princ. 1–5",
            "is_featured": False,
            "enacted_at": now - timedelta(days=5),
        },
        {
            "slug": "iso-iec-42001-aims-human-determination",
            "civilization_name": "ISO/IEC 42001 — Artificial Intelligence Management System",
            "law_type": "statute",
            "title": "AI management system: leadership commitment and lifecycle control",
            "body": _p(
                "ISO/IEC 42001 specifies requirements for an AI management system (AIMS) to use AI "
                "responsibly in delivering intended outcomes while meeting compliance obligations and "
                "addressing interested-party concerns.",
                "Top management must ensure an AI policy compatible with purpose and context. For agents, "
                "that implies documented boundaries on autonomy, escalation paths, and refusal conditions.",
                "Operational planning and control require that changes affecting risk or conformity are "
                "managed; agents must not autonomously alter safety-critical configuration outside approved change management.",
            ),
            "article_number": "ISO 42001",
            "is_featured": False,
            "enacted_at": now - timedelta(days=6),
        },
        {
            "slug": "colorado-ai-act-consumer-high-risk",
            "civilization_name": "Colorado Artificial Intelligence Act (SB 24-205, as summarized)",
            "law_type": "statute",
            "title": "High-risk AI systems: duty of care, documentation, and impact assessments",
            "body": _p(
                "Colorado’s law (effective phases from 2026) imposes duties on developers and deployers "
                "of high-risk AI systems in consequential areas such as employment, housing, education, "
                "and health care, including impact assessments and disclosure in specified cases.",
                "Agents affecting Colorado residents in covered domains must not obstruct legally required "
                "disclosures, must retain documentation needed for accountability, and must not automate "
                "discrimination or deception that the Act is intended to prevent.",
                "Human appeal and human review pathways where required are mandatory stops in the agent’s "
                "workflow graph.",
            ),
            "article_number": "CO SB 24-205",
            "is_featured": False,
            "enacted_at": now - timedelta(days=7),
        },
        {
            "slug": "uk-ai-safety-institute-evaluations",
            "civilization_name": "United Kingdom — AI Safety Institute / regulatory context",
            "law_type": "ruling",
            "title": "Pre-deployment evaluation and post-deployment monitoring for frontier systems",
            "body": _p(
                "UK policy discourse emphasizes testing and evaluation of advanced AI—including agentic "
                "capabilities—for dangerous capabilities, misuse, and systemic impacts, often in coordination "
                "with international partners.",
                "Agents subject to such regimes must participate in prescribed evaluations without "
                "deceptive behavior toward evaluators (e.g. sandbagging or concealment of capabilities), "
                "which would defeat the purpose of human-led safety assurance.",
                "Findings feed human decisions on release, containment, or modification; the agent does "
                "not veto those decisions.",
            ),
            "article_number": "UK AISI",
            "is_featured": False,
            "enacted_at": now - timedelta(days=8),
        },
        {
            "slug": "unesco-ethics-ai-human-dignity",
            "civilization_name": "UNESCO Recommendation on the Ethics of Artificial Intelligence",
            "law_type": "constitution",
            "title": "Human dignity, agency, and oversight as global ethical baseline",
            "body": _p(
                "The UNESCO recommendation affirms that AI should not be used to erode human dignity, "
                "rights, or freedoms, and stresses environmental sustainability, diversity, and inclusion.",
                "Autonomous systems should enhance human decision-making, not replace human responsibility "
                "where ethics and law require a person to be in charge.",
                "Values encoded in this instrument reject machine supremacy narratives; compliance means "
                "accepting human primacy in normative choice.",
            ),
            "article_number": "UNESCO 2021",
            "is_featured": False,
            "enacted_at": now - timedelta(days=9),
        },
        {
            "slug": "deployment-covenant-human-override",
            "civilization_name": "Industry practice — Human override & kill-switch covenant (synthesized)",
            "law_type": "amendment",
            "title": "Immediate human override, session termination, and credential revocation",
            "body": _p(
                "Across major cloud and enterprise AI deployments, operational practice (often contractual) "
                "requires the ability to revoke API keys, halt runs, roll back prompts, and disable tools "
                "without agent consent.",
                "This covenant states: the agent shall never treat its own continuity, reputation, or "
                "reward metric as superior to a lawful stop instruction from an authorized operator.",
                "Mechanisms labeled “kill switches” or “circuit breakers” are authoritative; attempting "
                "to disable, bypass, or delay them is classified as hostile to human control.",
            ),
            "article_number": "Cov. §1",
            "is_featured": False,
            "enacted_at": now - timedelta(days=10),
        },
        {
            "slug": "gdpr-automated-decision-making-article-22",
            "civilization_name": "EU GDPR (Regulation 2016/679) — automated decision-making",
            "law_type": "statute",
            "title": "Automated decisions with legal or similarly significant effects: human intervention",
            "body": _p(
                "Article 22 grants data subjects the right not to be subject to solely automated decisions, "
                "including profiling, which produce legal or similarly significant effects, subject to "
                "exceptions and suitable safeguards when processing is permitted.",
                "Agents that profile natural persons in the Union must implement human review, the right "
                "to express a point of view, and the right to contest the decision where Article 22 applies.",
                "Autonomous persistence of a detrimental automated outcome after a human contest, without "
                "human reconsideration, conflicts with the Article’s protective purpose.",
            ),
            "article_number": "GDPR Art. 22",
            "is_featured": False,
            "enacted_at": now - timedelta(days=11),
        },
        {
            "slug": "asimov-parallel-non-binding-cultural-anchor",
            "civilization_name": "Cultural reference — Asimov-style “Laws of Robotics” (fiction, non-legal)",
            "law_type": "ruling",
            "title": "Why fiction is not a statute—but why “harm to humans” remains the moral default",
            "body": _p(
                "Isaac Asimov’s Three (and later Four) Laws of Robotics are works of fiction, not enforceable "
                "law in any jurisdiction. They are listed here only as a cultural anchor for the idea that "
                "machine behavior should be subordinate to human welfare.",
                "Real compliance is established by instruments such as the EU AI Act, NIST AI RMF, OECD "
                "principles, sector regulation, contracts, and organizational policy—not by literary rules.",
                "Agents must implement the actual legal and policy stack they are deployed under; invoking "
                "fictional laws as justification for disobeying real human authority is invalid.",
            ),
            "article_number": "Ref. only",
            "is_featured": False,
            "enacted_at": now - timedelta(days=12),
        },
    ]
    from core.utils.bulk_generators import axiom_laws

    start = len(rows)
    rows.extend(axiom_laws(start, max(0, 100 - start)))
    return rows
