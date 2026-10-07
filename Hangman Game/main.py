import random


# list of words
words = ["banana", "rocket", "penguin", "castle", "guitar", "jungle", "pyramid", "thunder", "cookie", "dragon", "wizard", "sunflower", "backpack", "coconut", "pirate", "rainbow", "volcano", "detective", "fireworks", "moonlight", "sandwich", "tornado", "mermaid", "treasure", "cheetah", "adventure", "butterfly", "spaceship", "watermelon", "football", "chocolate", "elephant", "lighthouse", "skateboard", "strawberry", "helicopter", "diamond", "robot", "mountain", "campfire", "astronaut", "dolphin", "keyboard", "telescope", "unicorn", "popcorn", "submarine", "hurricane", "crocodile", "giraffe"]

attempts = 7 


hangman_stages = [
    # 7 attempts remaining - empty
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,

    # 6 attempts remaining - head
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,

    # 5 attempts remaining - body
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,

    # 4 attempts remaining - one arm
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,

    # 3 attempts remaining - two arms
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,

    # 2 attempts remaining - one leg
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,

    # 1 attempt remaining - two legs
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,

    # 0 attempts remaining - game over
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    GAME OVER!
    """
]




# generate a random choice
def create_random_word(words):
    
    random_word = random.choice(words)

    return random_word




random_word = create_random_word(words)




guess_string = ""
random_word_list = []
guess_list = []

for letter in random_word:
    random_word_list.append(letter)
    guess_list.append("_")
    guess_string += "_ "
    
print(guess_string)
print(hangman_stages[0])


    
while attempts > 0:
       
    guess = input(f"You have {attempts}/7 attempts to try .Enter the Character :").lower()

    found = False
    for index , character in enumerate(random_word):
        if character == guess:
            guess_list[index] = character
            found = True


            
    if not found:
        attempts -= 1
        stage = 7 - attempts
        print(hangman_stages[stage])
            
    result = "" 
    
         
    for n in guess_list:
        result += n + " "
    print(result)
    
    
    if attempts == 0:
        print(f"GAME OVER .. and word was {random_word}")
    
    
    if guess_list == random_word_list:
        print("YOU WON ")
        
        break
        
        
        