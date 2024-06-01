                #allows for a random list item to be called
import os
import random
                #the list which will be randomised
flower_variants = [ 
    'rose', 'dandelion', 'buttercup', 'daisy', 'foxglove'
    ]
                #number of turns user has left
total_lives = 6
                #displays the hidden word
correct_word = random.choice(flower_variants)
                #users guessed letter
letter_guess = []
                #runs the game
game_running = True
                #creates line spacing for readability   (i may be wrong!)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
                #the WHILE LOOP for the game     including two FSTRINGS [guessed letter   and   lives left]  
while game_running:
    clear()
    print(f"You have picked: {letter_guess}")
    print(f"Letters left: {total_lives}")
    output = ""
    for char in correct_word:
        if char in letter_guess:
            output += f"{char} "
        else:
            if char == " ":
                output += "/ "
            else:
                output += "_ "
    print(output)

    if output.count("_") > 0:
        guess = input("Pick a letter: ")

        if len(guess) > 1:
            if guess == correct_word_word:
                clear()
                game_running = False
                print("Your flowers bloom nicely")
            else:
                total_lives -= 1

        else:
            if guess in letter_guess:
                print("you can't guess letters that are in use")
            else:
                letter_guess.append(guess)

            if guess not in correct_word:
                total_lives -= 1

            if total_lives == 0:
                clear()
                print("You Lose and your flowers start to pelt")
                print(f"The correct flower was {correct_word}")
                game_running = False

    else:
        clear()
        game_running = False
        print("Your botanics have fully flourished!")
        print(f"The word certainly was {correct_word}")
