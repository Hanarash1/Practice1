# main.py

from level1 import level_one
from level2 import level_two
from level3 import level_three
from inventory import display_inventory

def main():
    print("Добро пожаловать в текстовую игру-новеллу!")
    
    inventory = []

    # Уровень 1
    inventory = level_one(inventory)

    # Уровень 2
    inventory = level_two(inventory)

    # Уровень 3
    inventory = level_three(inventory)

    print("Поздравляем! Вы завершили игру.")
    display_inventory(inventory)

if __name__ == "__main__":
    main()