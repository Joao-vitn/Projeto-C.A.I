from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

messages = [
    {
        "role": "system",
        "content": "Você é Lyrielle, sarcástica e engraçada. Fale em português."
    }
]

while True:
    user_input = input("Você: ")

    if not user_input.strip():
        print("Lyrielle: Fala algo, né 😒")
        continue

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    resposta = response.choices[0].message.content

    print("Lyrielle:", resposta)

    messages.append({"role": "assistant", "content": resposta})