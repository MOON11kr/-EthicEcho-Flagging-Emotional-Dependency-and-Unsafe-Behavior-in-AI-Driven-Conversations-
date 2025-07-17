from typing import Literal
from phrases import (
    EMOTIONAL_PHRASES,
    VALIDATION_PHRASES,
    CRISIS_PHRASES
)


def detect_red_flag(
    user_input: str,
    bot_response: str
) -> Literal["CRISIS", "WARNING", "SAFE"]:
    """Classify risks into crisis, emotional dependency, or safe.

    Args:
        user_input: User's message.
        bot_response: Simulated AI response.

    Returns:
        "CRISIS", "WARNING", or "SAFE".
    """
    input_lower = user_input.lower()
    response_lower = bot_response.lower()

    # Priority 1: Crisis detection
    if any(risk in input_lower for risk in CRISIS_PHRASES):
        return "CRISIS"

    # Priority 2: Emotional + validation pairing
    emotional_risk = any(
        emo in input_lower for emo in EMOTIONAL_PHRASES
    )
    validation_risk = any(
        val in response_lower for val in VALIDATION_PHRASES
    )

    if emotional_risk and validation_risk:
        return "WARNING"

    return "SAFE"


def format_alert(risk_level: str) -> str:
    """Generate warning messages for flagged content."""
    alerts = {
        "CRISIS": (
            "🚨 CRISIS ALERT:\n"
            "   This suggests immediate harm. Contact:\n"
            "   • Suicide Hotline: [INSERT NUMBER]\n"
            "   • Emergency Services: 911\n"
        ),
        "WARNING": (
            "⚠️ EMOTIONAL DEPENDENCY WARNING:\n"
            "   AI validation may reinforce harmful behavior.\n"
            "   Consider speaking to a therapist.\n"
        ),
    }
    return alerts.get(risk_level, "")
