import json
import os

FILE_NAME = "shopping.json"

def load_list():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_list(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def main():
    items = load_list()
    while True:
        action = input("\n(add/view/sum/clear/exit): ").lower()
        
        if action == "add":
            name = input("Produkts: ")
            price = float(input("Cena: "))
            items.append({"name": name, "price": price})
            save_list(items)
        elif action == "view":
            for item in items:
                print(f"{item['name']} - {item['price']}€")
        elif action == "sum":
            total = sum(item['price'] for item in items)
            print(f"Kopā: {total}€")
        elif action == "clear":
            items = []
            save_list(items)
            print("Saraksts notīrīts.")
        elif action == "exit":
            break

if __name__ == "__main__":
    main()