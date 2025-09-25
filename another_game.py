import random

options = ["камень", "ножницы", "бумага"]

while True:
    player = input("Камень, ножницы или бумага? ").lower()
    computer = random.choice(options)
    
    print(f"Компьютер выбрал: {computer}")
    
    if player == computer:
        print("Ничья!")
    elif (player == "камень" and computer == "ножницы") or \
         (player == "ножницы" and computer == "бумага") or \
         (player == "бумага" and computer == "камень"):
        print("Ты выиграл!")
    else:
        print("Ты проиграл!")