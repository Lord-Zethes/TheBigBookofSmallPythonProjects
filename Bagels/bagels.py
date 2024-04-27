import random
PLAY = True
NUMBER_DIGITS = 3
MAX_GUESS = 10

def GameRules():
    """This function prints the greeting and rules of the game"""
    print('          Bagels Is a deductive logic game.\n'
        'I am thinking of a 3 digit number. Try to guess what it is.\n'
        'Here are some clues:\n'
        '\n'
        '      When I Say      |       That means\n'
        '      Pico            |       One Digit is correct but in the wrong position\n'
        '      Fermi           |       One digit is correct and in the right position\n' 
        '      Bagels          |       No digit is correct\n'   
        '\n'
        'For Example, if the secret number was 248 and your guess was 843, the\n'
        'clues would be Fermi Pico' .format(NUMBER_DIGITS) 
    )

def RandomNumber():
    """Gets a number and returns it as a sting for compairing to input"""
    numbers = list('0123456789')
    random.shuffle(numbers)
    random_number = ''
    for i in range(NUMBER_DIGITS):
        random_number += str(numbers[i])
    return random_number

def Clues(guess, randnumber):
    hint = []
    if guess == randnumber:
        return 'You got it!'
    for i in range(len(guess)):
        if guess[i] == randnumber[i]:
            hint.append('Fermi')
        elif guess[i] in randnumber:
            hint.append('Pico')
    if len(hint) == 0:
        return 'Bagel'
    else:
        hint.sort()
        return ''.join(hint)
    

def BuiltGame():
    GameRules()
    while True:
        randomint = RandomNumber()
        print('The Number has been selected!')
        print(f'you have {MAX_GUESS} guesses to get it.')
        numofguesses = 1
        while numofguesses <= MAX_GUESS:
            guess = ''

            while len(guess) != NUMBER_DIGITS or not guess.isdecimal():
                print(f'Guess #{numofguesses}')
                guess = input()

            hints = Clues(guess, randomint)
            print(hints)
            numofguesses += 1

            if guess == randomint:
                    break
            if numofguesses > MAX_GUESS:
                print("you lose")
                print(f'The correct guess was {randomint}')
        print("do you want to play agian? (yes or no)")
        if not input('>').lower().startswith("y"):
                break
        print("thanks for playing")


BuiltGame()