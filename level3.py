# level3.py

def level_three(inventory):
    print("Вы в тронном зале. Здесь вас ждет дракон! У вас есть меч.")
    
    # Проверяем, есть ли у игрока меч
    if "меч" in inventory:
        while True:
            action = input("Введите команду (атаковать дракона, показать инвентарь): ").lower()
            
            if action == "атаковать дракона":
                print("Вы победили дракона с помощью меча!")
                break
            elif action == "показать инвентарь":
                print("Ваш инвентарь:", ", ".join(inventory))
    else:
        print("У вас нет меча, чтобы сразиться с драконом.")
    
    return inventory  # Возвращаем инвентарь для завершения игры