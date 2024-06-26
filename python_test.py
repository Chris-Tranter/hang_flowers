                #allows for a random list item to be called
import os
import random
                #the list which will be randomised
flower_variants = [ 
    'rose', 'dandelion', 'buttercup', 'daisy', 'foxglove', 'Aster', 'Azalea',
    'Bergamot', 'camelia', 'lily', 'carnation', 'chicory', 'chrysanthemum',
    'cyclamen', 'freesia', 'french marigold', 'fuchsia', 'gardenia', 'grape hyacinth', 'heather',
    'hibiscus', 'holly', 'honeysuckle', 'hyacinth', 'hydrangea', 'honeysuckle', 'poppy', 'iris',
    'honeysuckle', 'jasmine', 'kangaroo paw', 'lavender', 'lotus', 'love in the mist', 'marigold',
    'orchid', 'poppy', 'petunia', 'sunflower', 'cauliflower' 
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
            if guess == correct_word:
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
        print(f"Yes, {correct_word} was correct, and it has bloomed nicely!")
