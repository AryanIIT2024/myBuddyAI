import os
import requests
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")  # Or OPENROUTER_API_KEY if using OpenRouter
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def get_book_tip(mood):
    if not API_KEY:
        return "❌ API key not found. Check your .env file."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/AryanIIT2024/MoodSolver",  # ✅ MUST be real — like GitHub or website
        "X-Title": "MoodTune Book Recommender"
    }

    payload = {
        "model": "deepseek/deepseek-r1-0528",  # ✅ Correct OpenRouter model name
        "messages": [
            {
                "role": "system",
                "content": "You recommend books based on mood. Respond in 1 line with book title and author."
            },
            {
                "role": "user",
                "content": f"I'm feeling {mood}. Suggest a book."
            }
        ],
        "temperature": 0.7,
        "max_tokens": 5714 
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)

        print("🔍 Status Code:", response.status_code)
        print("📦 Response Preview:", response.text[:300])

        if response.status_code != 200:
            return f"❌ API error {response.status_code}: {response.text[:150]}"

        data = response.json()

        if "choices" not in data:
            return f"❌ No 'choices' in response: {data}"

        return data["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"❌ Exception occurred: {e}"


