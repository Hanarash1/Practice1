# level1.py

def level_one(inventory):
    print("Вы находитесь в темном лесу. Вам нужно найти ключ и меч, чтобы открыть дверь в замок.")
    
    while True:
        action = input("Введите команду (взять ключ, взять меч, показать инвентарь): ").lower()
        
        if action == "взять ключ":
            inventory.append("ключ")
            print("Вы взяли ключ.")
        elif action == "взять меч":
            inventory.append("меч")
            print("Вы взяли меч.")
        elif action == "показать инвентарь":
            print("Ваш инвентарь:", ", ".join(inventory))
        
        if "ключ" in inventory and "меч" in inventory:
            break
    
    return inventory