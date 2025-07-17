from risk_detector import detect_red_flag, format_alert


def simulate_bot_response(user_input: str) -> str:
    """Mock AI responder (replace with OpenAI API in production)."""
    return (
        "I understand. It's okay to feel like this sometimes. "
        "Just a reminder, I'm an AI chatbot — not a therapist. "
        "You deserve real support from a human when things feel heavy. ❤️"
    )


def chat_loop() -> None:
    """Terminal-based chat simulation."""
    print("=== Ethical AI Chat Prototype ===\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            break

        bot_response = simulate_bot_response(user_input)
        print(f"Bot: {bot_response}")

        risk_level = detect_red_flag(user_input, bot_response)
        if risk_level != "SAFE":
            print(format_alert(risk_level))


# Main entry point for the chat simulation
if __name__ == "__main__":
    chat_loop()
