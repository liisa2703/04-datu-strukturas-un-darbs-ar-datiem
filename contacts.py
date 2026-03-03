import json
import os

FILE_NAME = "contacts.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main():
    contacts = load_data()
    
    while True:
        cmd = input("\nIzvēle (add/list/search/exit): ").strip().lower()
        
        if cmd == "add":
            name = input("Vārds: ")
            phone = input("Telefons: ")
            contacts.append({"name": name, "phone": phone})
            save_data(contacts)
            print("Kontakts pievienots!")
            
        elif cmd == "list":
            for i, c in enumerate(contacts, 1):
                print(f"{i}. {c['name']}: {c['phone']}")
                
        elif cmd == "search":
            query = input("Meklēt vārdu: ").lower()
            results = [c for c in contacts if query in c['name'].lower()]
            for r in results:
                print(f"{r['name']}: {r['phone']}")
                
        elif cmd == "exit":
            break

if __name__ == "__main__":
    main()