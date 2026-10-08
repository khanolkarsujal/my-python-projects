import random


# Computer's turn
def computer_choice(current_number):

    random_num = random.randint(1, 3)
    computer_choice_list = []

    for i in range(random_num):

        if current_number > 21:
            break

        computer_choice_list.append(current_number)
        current_number += 1

    return computer_choice_list, current_number


# User's turn
def user_choice(current_number):

    while True:

        user_input = input(
            "Enter next number(s) separated by space (1-3 numbers): "
        )

        user_input = user_input.split()

        # Check number of inputs
        if len(user_input) > 3 or len(user_input) == 0:
            print("Try again... enter 1 to 3 numbers.")
            continue

        # Check that every input is a number
        if not all(num.isdigit() for num in user_input):
            print("Try again... enter numbers only.")
            continue

        # Convert strings to integers
        user_numbers = []

        for num in user_input:
            user_numbers.append(int(num))

        # Check that numbers are consecutive
        expected_number = current_number

        valid = True

        for num in user_numbers:

            if num != expected_number:
                valid = False
                break

            expected_number += 1

        if not valid:
            print("Try again... enter the numbers in sequence.")
            continue

        # Valid input
        current_number += len(user_numbers)

        return current_number


# Game starts
current_number = 1

while True:

    # Computer turn
    computer_choose, current_number = computer_choice(current_number)

    print("Computer:", *computer_choose)

    # Check game over
    if current_number >= 21:
        print("GAME OVER")
        break

    # User turn
    current_number = user_choice(current_number)

    print("Current number:", current_number)

    # Check game over
    if current_number >= 21:
        print("GAME OVER")
        break