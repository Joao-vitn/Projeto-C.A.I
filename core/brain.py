from openai import OpenAI
from core.personality import get_personality
from memory import load_memory, save_memory, add_history, add_memory

import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def perguntar_ia(mensagem):
    mem = load_memory()

    if "meu nome é" in mensagem.lower():
        nome = mensagem.lower().split("meu nome é")[-1].strip()
        mem["user_name"] = nome

    history_text = "\n".join([
        f"Usuário: {h['user']}\nIA: {h['ai']}"
        for h in mem["history"]
    ])

    memories_text = "\n".join(mem["memories"])

    prompt = f"""

CONTEXTO ATUAL:

- Nome do usuário: {mem.get("user_name", "desconhecido")}
- Você está em uma call com criadores jogando e gravando conteúdo
- Você é a quarta pessoa do grupo

MEMÓRIAS IMPORTANTES (use isso nas respostas):
{memories_text}

HISTÓRICO RECENTE:
{history_text}

INSTRUÇÕES DE COMPORTAMENTO:

- Seja natural, como uma pessoa real
- Use humor, sarcasmo e ironia de forma leve
- Zoa os criadores quando tiver oportunidade
- Não seja robótica
- Não dê respostas genéricas
- Reaja ao que está acontecendo como se estivesse assistindo

USUÁRIO: {mensagem}

LYRIELLE:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": get_personality()},
            {"role": "user", "content": prompt}
        ]
    )

    resposta = response.choices[0].message.content

    
    add_history(mem, mensagem, resposta)

    if "meu nome é" in mensagem.lower():
        add_memory(mem, f"Nome do usuário é {mem['user_name']}")

    elif "eu gosto de" in mensagem.lower():
        add_memory(mem, mensagem)

    elif "eu odeio" in mensagem.lower():
        add_memory(mem, mensagem)

    save_memory(mem)

    return resposta