import memory.json
import os

memory_file = "memory/storage.json"

# carregar
def load_memory():
    if not os.path.exists(memory_file):
         return {
            "user_name": "User",
            "bond": 0.3,
            "memories": [],
            "history": []
        }
    with open(memory_file, "r")as f:
         return json.load(f)
    
    #salvar
def save_memory(mem):
     with open(memory_file, "w") as f:
          json.dump(mem,f, indent=4)

    #histórico (curto prazo)

def add_to_history(mem, user, ai):
    mem["history"].append({
        "user": user,
        "ai": ai
    })
    
    #Mantém só as ultimas 10 interações
    if len(mem["history"]) > 10:
         mem["history"].pop(0)

    #histórico longo prazo
def store_memory(mem, text):
    if len(text) > 15:
        mem["memories"].append(text)

    # limite pra não crescer infinito
    if len(mem["memories"]) > 50:
        mem["memories"].pop(0)