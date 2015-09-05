import random


with open('/usr/share/dict/words') as w:
    word_list = w.read()
    word_list = word_list.split()

def easy_words(word_list):
    easy_words_list = []
    for word in word_list:
        if 4 <= len(word) <= 6:
            easy_words_list.append(word)
    word = random.choice(easy_words_list)
    return word

def medium_words(word_list):
    medium_words_list = []
    for word in word_list:
        if 6 <= len(word) <= 8:
            medium_words_list.append(word)
    word = random.choice(medium_words_list)
    return word

def hard_words(word_list):
    hard_words_list = []
    for word in word_list:
        if 8 <= len(word):
            hard_words_list.append(word)
    word = random.choice(hard_words_list)
    return word

def random_word(word_list):
    word = random.choice(word_list)
    return word



def display_word(word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.

    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.

    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.
    """
    # TODO
    pass


def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    # TODO
    pass


def main():
    """
    Runs when the program is called from the command-line.

    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
    3. Performs the game loop, consisting of:
       a. Printing the word in progress, using _ for unguessed letters
       b. Printing the number of guesses remaining
       c. Printing the letters that have been guessed so far
       d. Prompting the user for a letter to guess
    4. Finishing the game and displaying whether the user has won or lost
    5. Giving the user the option to play again
    """
    # TODO


if __name__ == '__main__':
    main()
