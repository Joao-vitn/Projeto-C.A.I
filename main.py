from core.brain import perguntar_ia

print("=== Lyrielle acordou! ===")

while True:
    pergunta = input("Você: ")

    if pergunta.strip().lower() in ["sair", "exit", "quit", "tchau", "fim"]:
        print("Lyrielle: Até logo! 😏")
        break

    resposta = perguntar_ia(pergunta)
    print(f"Lyrielle: {resposta}")