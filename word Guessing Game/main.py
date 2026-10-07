import random


# words list
words = [
    "apple",
    "banana",
    "mango",
    "orange",
    "grape",
    "watermelon",
    "computer",
    "python",
    "programming",
    "keyboard",
    "mouse",
    "internet",
    "school",
    "college",
    "student",
    "teacher",
    "doctor",
    "engineer",
    "car",
    "bike",
    "train",
    "airplane",
    "house",
    "garden",
    "river",
    "mountain",
    "ocean",
    "sun",
    "moon",
    "star"
]

# random word 
random_word = random.choice(words)


print(random_word)

random_letter = []
guess_char = []

for letter in random_word:
    random_letter.append(letter)
    guess_char.append("_")



def create_str(guess_char):
    str_guess_char = ""
    for letter in guess_char:
        str_guess_char += letter + " "
    print(str_guess_char)

create_str(guess_char)


attempts = 7

while attempts > 0:
    guess = input("\nGuess the characters :")


            
    found = False

    for index , character in enumerate(random_letter):

        
        if character == guess:
            guess_char[index] = guess
            found = True


    if not found:
        attempts -= 1
        print(f"you have {attempts} to try ..")

    if "_" not in guess_char:
        print("YOU WON !")
        break


    create_str(guess_char)
   

if attempts == 0 :
    print(f"GAME OVER and .. word was {random_word}")