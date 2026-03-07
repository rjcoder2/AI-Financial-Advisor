from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("Loaded API key:", api_key)



from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("Loaded API key:", api_key)

# Use the new client
from google.genai import Client

client = Client(api_key=api_key)

try:
    response = client.generate_text(
        model="gemini-1.5",
        prompt="Test connectivity with Gemini API"
    )
    print("Gemini Response:", response.text)
except Exception as e:
    print("⚠️ Gemini API error:", e)
