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
    # take the word, split it apart into a list of its letters.
    # start with a variable with nothing in it. this will be new each time.
    # go through each letters in word
    # if letter is in guesses: .append the letter
    # if letter is not in guesses: add the letter as '_'
    # add letter/'_' of the word in sequence with a space
    # return the word and uppercase the letters


    word_onscreen = []
    for letter in word:
        if letter in guesses:
            word_onscreen.append(letter)
        else:
            word_onscreen.append('_')
    word_onscreen = ' '.join(word_onscreen)
    return word_onscreen.upper()



def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    # go through each letter of the word
    # if the letter is not in guesses then False
    # if you don't get any false, then you can consider True

    for letter in word:
        if letter not in guesses:
            return False
    return True


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

    print("      ")
    print(" The Mystery Word Challenge ")
    levelselect()


def levelselect():
    level = 0
    if level not in ("1", "2", "3", "4"):

        level = input("""What level do you want to play at?
        1 - Easy 4-6 letters
        2 - Medium 6-8 letters
        3 - Hard 8 + letters
        4 - QUIT

        Enter a number 1-4 to start   """)

    if level == 4:
        print("Thanks for playing the game.")
        exit()
    if level == 1:
        word = easy_words(word_list)
    if level == 2:
        word = medium_words(word_list)
    if level == 3:
        word = hard_words(word_list)
    print("Your word is {} letters long.".format(len(word)))


def gameplay():
    pass


def replaygame():
    while True:
        response = input("Do you want to play the game again?  'y' or 'n' ?")
        if response == 'y':
            levelselect()
        elif response == 'n':
            print("Thanks for playing the game.")
            exit()
        else:
            continue



if __name__ == '__main__':
    main()
