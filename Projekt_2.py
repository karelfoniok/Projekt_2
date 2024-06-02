"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Karel Foniok
email: karel.foniok@gmail.com
discord: karel_10181
"""

import random

separator = 50 * "-"
welcome = print(f"Hi there!", separator,
                    "I've generated a random 4 digit number for you.",
                    "Let's play a bulls and cows game.",
                    separator,
                    "Enter a number:",
                    separator, sep="\n")

def random_number():
    '''
    generates random four digit number with unique digits
    '''
    number = str(random.randint(1000,9999))
    while len(number) != len(set(number)):         
        number = str(random.randint(1000,9999))
    return number
           
def players_input_check(input):
    '''
    Check if players guess is in line with rules of the game and does NOT:
    - have more or less digits than 4
    - contain same digits
    - start with 0
    - contain charactares other than digits
    '''
    if len(input) != 4 or not input.isdigit():
        print(f"That's not a four digit number. Try again")
        return False
    elif len(input) != len(set(input)):
        print(f"You cannot input same digit twice. Try again")
        return False
    elif input[0] == "0":
        print(f"The number cannot start with zero. Try again")
        return False
    else:
        return True
    
def bulls_and_cows_count(random_number, guess):
    '''
    From player's guess calculates number of bulls and cows
    '''
    bulls = 0
    cows = 0
    for i, digit in enumerate(guess):
        if random_number[i] == digit:
            bulls += 1
        elif digit in random_number:
            cows += 1
    return bulls, cows   

def scorecard(number_of_attempts):
    '''
    number of attempts to take the player to finish the game
    '''
    if number_of_attempts <= 5:
        print(f"Amazing score")
    elif number_of_attempts <= 10:
        print(f"Well done")
    elif number_of_attempts <= 15:
        print(f"Not too bad")
    else:
        print(f"Time to practice")

def game():
    '''
    let's play the game
    '''
    #welcome the  player
    welcome
    #generate random number
    number = random_number()
    
    attempts = 0

    # guess the right number
    while True:
        guess = input(">>> ")
        print(separator)
        attempts += 1

        if players_input_check(guess):
            if guess == number:
                print(f"Correct, you've guessed the right number in {attempts} guesses!")
                break
            else:
                bulls, cows = bulls_and_cows_count(number, guess)
                if bulls == 1 and cows == 1:
                    print(f"{bulls} bull and {cows} cow")
                elif bulls == 1:
                    print(f"{bulls} bull and {cows} cows")
                elif cows == 1:
                    print(f"{bulls} bulls and {cows} cow")
                else:
                    print(f"{bulls} bulls and {cows} cows")

    print(separator)
    scorecard(attempts)
                        
if __name__=="__main__":
    game()


