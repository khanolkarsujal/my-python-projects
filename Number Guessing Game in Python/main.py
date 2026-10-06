import random


# generating a random
random_number = random.randint(1,100)

# Attempts 
attemps = 7 

while attemps > 0:
    guess = int(input("Enter the guess number :"))



    if guess == random_number:
        print(f"YOU WON ... YOU FOUND THE NUMBER '{random_number}'")
        break

    elif guess > random_number:
        attemps -= 1
        print(f"Try a lower number .. and have {attemps} attemps left to try ..\n")

    elif guess < random_number:
        attemps -= 1
        print(f"Try a higher number .. and you have {attemps} attemps left to try ..\n")

    if attemps == 0:
        print("GAME OVER..\n")
 