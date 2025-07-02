import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Create OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def enhanced_motivation(user_mood, user_reason=None, user_tone="gentle", user_length="short"):
    prompt = f"""
You are a daily motivation generator that gives personalized motivational quotes/messages.

The user will give you:
- Mood or situation
- Optional reason (e.g., "exam tomorrow", "struggling with goals")
- Preferred tone (gentle, bold, poetic)
- Preferred length (short: <30 words, medium: ~50 words, long: 80+ words)

Your task is to craft a powerful, emotionally resonant motivational message based on this input.

Now generate a motivational message for:

- Mood: {user_mood}
- Reason: {user_reason or "N/A"}
- Tone: {user_tone}
- Length: {user_length}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # use gpt-4 if you have access
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=150
    )

    return response.choices[0].message.content.strip()

# Example Usage:
if __name__ == "__main__":
    print(enhanced_motivation(
        user_mood="feeling lost",
        user_reason="not sure what direction my career is going",
        user_tone="poetic",
        user_length="medium"
    ))
