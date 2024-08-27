
import random

#words which are mountains in the world which have a peak
mountain_list = ('kilimanjaro', 'kenya', 'elgon', 'ras dashen', 'meru', 'simien',
                 'rwenzori', 'drakensberg', 'toubkal', 'cameroon', 'everest', 'fuji',
                 'denali', 'elbrus', 'montblanc', 'matterhorn', 'aconcagua', 'vinson',
                 'kosciuszko', 'eiger', 'annapurna', 'lhotse', 'makalu',)

#misses holds the number of chances the player gets to guess the word
misses = 6

#based on the number of misses it will display the current state of the hangman in the hangman stages
hangman_stages = [
    """
    -----
    |   |
        |
        |
        |
        |
    """,
    """
    -----
    |   |
    O   |
        |
        |
        |
    """,
    """
    -----
    |   |
    O   |
    |   |
        |
        |
    """,
    """
    -----
    |   |
    O   |
   /|   |
        |
        |
    """,
    """
    -----
    |   |
    O   |
   /|\\  |
        |
        |
    """,
    """
    -----
    |   |
    O   |
   /|\\  |
   /    |
        |
    """,
    """
    -----
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    """
]

#computer chooses a random word from the list
chosen_word = random.choice(mountain_list)

#empty display list that will hold current state of the guessed word
display = []

#empty set to keep track of letters already chosen
guessed_letters = set()

#display has underscores for each  letter in chosen word
for i in range (len(chosen_word)):
    display += '_'
print('Hello! Welcome to the Hangman game.')
print('A mountain that has a peak')
print (display)

#while loop for when the misses have not yet reached zero
while misses > 0:
    try:
        guessed_letter = input('Guess a letter: ').lower()

#if statements to check whether a letter is the input and ensure the letter is not repeated
        if len(guessed_letter) != 1 or not guessed_letter.isalpha():
            print('Incorrect input, please enter a single letter')
            continue
        if guessed_letter in guessed_letters:
            print('You have already guessed that letter')
            continue
        guessed_letters.add(guessed_letter)

#if else statement to check if the guessed letter is in the chosen word
        if guessed_letter in chosen_word:
            print('Correct you have guessed the right letter!')
            for position in range(len(chosen_word)):
                if chosen_word[position] == guessed_letter:
                    display[position] = guessed_letter
            print(''.join(display))
        else:
            misses -= 1
            print(f'Incorrect. {misses} turn(s) left.')
            print(''.join(display))
            print(hangman_stages[misses])

#checking if the player has won
        if '_' not in display:
            print(f'Congratulations, you win!. The word was: {chosen_word}')
            print('Game over, play again!')
            break
    except Exception as e:
        print(f'An error occurred: {e}')

#checking if the player has lost
    if misses == 0:
        print(f'You lose. The word was: {chosen_word}.')
        print(hangman_stages[misses])
        print('Game over, Try again')

