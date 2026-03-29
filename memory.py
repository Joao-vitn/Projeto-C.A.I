import json
import os

FILE= "memory.json"

def load_memory():
    if not os.path.exists(FILE):
        return {
            "history": [],
            "memories": []
        }
    
    with open(FILE, "r") as f:
        return json.load(f)


def save_memory(mem):
    with open(FILE, "w") as f:
        json.dump(mem, f, indent=4)


def add_history(mem, user, ai):
    mem["history"].append({
        "user": user,
        "ai": ai
    })

    if len(mem["history"]) > 5:
        mem["history"].pop(0)


def add_memory(mem, text):
    if len(text) > 10:
        mem["memories"].append(text)

    if len(mem["memories"]) > 10:
        mem["memories"].pop(0)