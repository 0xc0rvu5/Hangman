import random, os
from hangman_words import word_list
from hangman_art import logo, stages


#initialize relevant variables
DISPLAY = []
WORD = random.choice(word_list)
LENGTH = len(WORD)
END_OF_GAME = False
LIVES = 6


#determine word length and display by the means of underscores
for _ in range(LENGTH):
    DISPLAY += '_'


#initiate game loop
try:
    while not END_OF_GAME:
        print(logo)
        choice = input('Guess a letter: ').lower()

        #clear screen
        os.system('clear')

        #if choice is a duplicate
        if choice in DISPLAY:
            print(f'You have already guessed {choice}')

        #if choice is correct
        for i in range(LENGTH):
                letter = WORD[i]
                if letter == choice:
                    DISPLAY[i] = letter

        #if choice is wrong
        if choice not in WORD:
            LIVES -= 1
            print(f'{choice} was not in the word.')
            if LIVES == 0:
                END_OF_GAME = True
                print('**You lose.**')

        #convert list to string
        print(f'{" ".join(DISPLAY)}')

        #if all letters are filled in game contestant wins
        if "_" not in DISPLAY:
            END_OF_GAME = True
            print('~/!\~ You win. ~/!\~')
        
        #print remaining guesses/lives
        print(stages[LIVES])

except KeyboardInterrupt:
    print('\nSee you later.')