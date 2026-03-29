def build_prompt(mem, user_input):
    history = "\n".join([
        f"Usuário: {h['user']}\nIA: {h['ai']}"
        for h in mem["history"][-5:]
    ])

    memories = "\n".join(mem["memories"][-5:])

    prompt = f"""
Você é Lyrielle.

Memórias importantes:
{memories}

Histórico recente:
{history}

Usuário: {user_input}
Lyrielle:
"""
    return prompt