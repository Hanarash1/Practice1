# level2.py

def level_two(inventory):
    print("Вы у двери замка. Чтобы открыть ее, вам нужно решить загадку: 'Что всегда идет, но никогда не приходит?'")
    
    while True:
        answer = input("Ваш ответ: ").lower()
        
        if answer == "время":
            print("Вы открыли дверь!")
            break
        else:
            print("Неправильный ответ. Попробуйте снова.")
    
    return inventory  # Возвращаем инвентарь для продолжения игры