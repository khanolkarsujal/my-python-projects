import random


# generating a random
random_number = random.randint(1,100)

# Attempts 
attempts = 7 

while attempts > 0:

    

    while True:
        try:
            guess = int(input("Enter the guess number :"))
            break
        except ValueError:
            print("Please enter a valid number\n")

        

    if guess == random_number:
        print(f"YOU WON ... YOU FOUND THE NUMBER '{random_number}'")
        break

    elif guess > random_number:
        attempts -= 1
        print(f"Try a lower number .. and have {attempts} attempts left to try ..\n")

    elif guess < random_number:
        attempts -= 1
        print(f"Try a higher number .. and you have {attempts} attempts left to try ..\n")

    if attempts == 0:
        print(f"GAME OVER.. the random number was {random_number} \n")
 