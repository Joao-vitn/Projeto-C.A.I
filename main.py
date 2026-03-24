from core.brain import perguntar_ia

print("=== Lyrielle acordou! ===")

while True:
    pergunta = input("Você: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Lyrielle: Até logo! 😏")
        break
    
    resposta = perguntar_ia(pergunta)
    print(f"Lyrielle: {resposta}")

   

def build_prompt(mem, user_input):
    history = mem["history"][-5:]
    memories = mem["memories"][-5:]

    prompt = f"""
Você é uma IA companheira.

Memórias importantes:
{memories}

Histórico recente:
{history}

Usuário: {user_input}
IA:
"""
    return prompt