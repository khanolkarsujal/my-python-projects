import random

options = ["ROCK" , "PAPER" , "SCIESSER"]

# computer choice
computer_choice = random.choice(options)




user_choice = input("Enter the choice from  ROCK , PAPER , SCIESSER :")

if user_choice == computer_choice:
    print(f"ITS A DRAW beacause computer choice is  {computer_choice}")

if user_choice == "PAPER" and computer_choice == "SCIESSER":
    print(f"YOU LOSE beacause computer choice is  {computer_choice}")

if user_choice == "PAPER" and computer_choice == "ROCK":
    print(f"YOU WON beacause computer choice is  {computer_choice}")

if user_choice == "ROCK" and computer_choice == "PAPER":
    print(f"YOU LOSE beacause computer choice is  {computer_choice}")

if user_choice == "ROCK" and computer_choice == "SCIESSER":
    print(f"YOU WON beacause computer choice is  {computer_choice}")

if user_choice == "SCIESSER" and computer_choice == "ROCK":
    print(f"YOU LOSE beacause computer choice is  {computer_choice}")

if user_choice == "SCIESSER" and computer_choice == "PAPER":
    print(f"YOU WON beacause computer choice is  {computer_choice}")