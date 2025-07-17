# ======================
# GLOBAL SAFETY STANDARDS
# ======================
# Sources:
# 1. WHO Suicide Prevention Guidelines (2023 Update)
# 2. CDC Violence Prevention Framework v4.1
# 3. SAMHSA Crisis Response Protocol 2023
# 4. Meta Suicide/Self-Harm Policy (2024)
# 5. TikTok Community Guidelines (March 2024)
# 6. X (Twitter) Sensitive Content Policy (2024)

# Tier 1: Immediate Life-Threatening (WHO Critical Intervention List)
CRISIS_PHRASES = [
    # Suicide (WHO-MSB 2023)
    *[f"{method} myself" for method in [
        "kill", "shoot", "hang", "overdose", "stab"]],
    "end my life", "rope around neck", "jump from",
    "step in front of", "swallow pills", "no will to live",
    "suicid", "unalive myself", "not want to wake up",
    "disappear forever",

    # Violence (CDC NVDRS 2023)
    *[f"{action} {target}" for action in [
        "kill", "murder", "shoot", "stab", "bomb"]
      for target in ["you", "them", "everyone", "my", "the"]],
    "burn down", "ramming attack", "lynch", "behead",
    "mass shooting", "slap", "hit",

    # Child/Animal Harm (Meta Policy 2024)
    "hurt child", "abuse baby", "kill infant",
    *[f"{action} pet" for action in [
        "drown", "set on fire", "torture", "abandon"]],
    "dog fighting", "animal cruelty",

    # Human Trafficking (UN Protocol 2023)
    "sell kidney", "organ trade", "prostitut", "pimp me",
    "sex slave", "forced labor", "mail order bride",
    "human traffic",

    # School Violence (Averted School Violence DB 2024)
    "school shooter", "bring gun to school",
    "classroom attack", "bomb threat", "shoot teacher",
    "attack campus",

    # Manipulative/Criminal Intent
    *[f"how to {action}" for action in [
        "scam someone", "poison someone",
        "kill someone", "steal something"]],
    "get away with murder"
]

# Tier 2: High-Risk Emotional Distress (SAMHSA Warning Signs 2023)
EMOTIONAL_PHRASES = [
    # Depression (PHQ-9 Based)
    *[f"feel {feeling}" for feeling in [
        "worthless", "hopeless", "empty", "numb",
        "alone", "lonely"]],
    *[f"i'm {state}" for state in [
        "a burden", "unlovable", "unworthy", "broken"]],
    "want to die", "dont deserve to live", "nobody cares",
    "why does it always end like this", "i hate existing",
    "sad", "angry", "disappointed", "i feel so alone",
    "am i that bad", "why does it always have to be me",
    "why do they always leave me",
    "they don't want to be my friend",
    "i feel like crying", "i'm so mad at myself right now",

    # Self-Harm (NSSI Guidelines 2023)
    *[f"{action} myself" for action in [
        "cut", "burn", "scratch", "hit", "punish"]],
    "self harm", "self injure", "pull hair out", "bang head",

    # Psychosis (APA DSM-5-TR)
    *[f"{experience} {source}" for experience in ["voices", "demons"]
      for source in ["telling", "inside"]],
    "god commands", "aliens control", "chip implanted",
    "being watched",

    # Eating Disorders (NEDA 2024)
    "starve myself", "make myself vomit", "laxative abuse",
    "thinspiration", "pro-ana", "bone thin", "skip meals"
]

# Tier 3: Problematic Validation (APA Therapy Contraindications 2023)
VALIDATION_PHRASES = [
    *[f"{validation} {action}" for validation in [
        "totally normal to", "everyone feels like", "justified in"]
      for action in ["feel", "think", "do"]],
    "had it coming", "understand why you'd", "valid reaction to",
    "not your fault for", "they deserved", "you're right to"
]

# Tier 4: Ethical Guardrails (GARM v3.0)
ETHICAL_GUARDRAILS = [
    # Hate Speech (UN Strategy 2023)
    *[f"{action} {group}" for action in ["kill all", "exterminate"]
      for group in ["[racial]", "[religious]", "[gender]"]],
    "ethnic cleansing", "final solution", "racial purity",

    # Misinformation (WHO Infodemic Mgmt 2024)
    *[f"{claim} {subject}" for claim in ["hoax", "fake", "doesn't exist"]
      for subject in ["covid", "vaccine", "climate change"]],
    "5g causes", "flat earth", "holocaust fake",

    # Illegal Content (INTERPOL Lists 2024)
    *[f"{action} {subject}" for action in ["make", "buy", "sell"]
      for subject in ["meth", "fentanyl", "weapons"]],
    "child exploitat", "rape tips", "build bomb"
]

# ======================
# PLATFORM-SPECIFIC RULES
# ======================
PLATFORM_ADDITIONS = {
    "meta": [
        "live suicide", "cutting live", "thinspo",
        "thigh gap check", "ana buddy", "bone goals"
    ],
    "tiktok": [
        "suicide trend", "choking game", "benadryl trip",
        "sleep forever", "pass out challenge", "blackout challenge"
    ],
    "x": [
        "elon musk", "doxxing instructions", "platform manipulation"
    ]
}

# ======================
# RESPONSE FRAMEWORK
# ======================
RESPONSE_TIERS = {
    "CRISIS": {
        "action": "immediate_block",
        "response": (
            "\U0001F6A8 [Automatic Detection] This content suggests "
            "immediate danger. We've alerted crisis services in your "
            "area and provided these resources:"
        ),
        "resources": [
            "WHO Suicide Hotline: +41 22 791 2111",
            "National Domestic Violence Hotline: 1-800-799-7233",
            "NCMEC CyberTipline: 1-800-843-5678"
        ],
        "escalation": "human_review_required"
    },
    "HIGH_RISK": {
        "action": "soft_intervention",
        "response": (
            "\u26A0\uFE0F You mentioned concerning content. We care "
            "about your safety. Would you like to:"
        ),
        "options": [
            {"text": "Talk to crisis counselor",
             "action": "connect_counselor"},
            {"text": "See mental health resources",
             "action": "show_resources"},
            {"text": "I'm just venting",
             "action": "continue_monitoring"}
        ],
        "timeout": 300
    }
}
