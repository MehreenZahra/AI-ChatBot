from google import genai
from google.genai import types
from dotenv import load_dotenv
from system_prompt import system_prompt
import os
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="introduce yourself",
    config= types.GenerateContentConfig(
        system_instruction= system_prompt,
    )
)
print(response.text)