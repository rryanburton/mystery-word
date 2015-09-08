import random


with open('/usr/share/dict/words') as w:
    word_list = w.read()
    word_list = word_list.split()

def easy_words(word_list):
    easy_words_list = []
    for word in word_list:
        if 4 <= len(word) <= 6:
            easy_words_list.append(word)
    #word = random.choice(easy_words_list)
    return easy_words_list

def medium_words(word_list):
    medium_words_list = []
    for word in word_list:
        if 6 <= len(word) <= 8:
            medium_words_list.append(word)
    # word = random.choice(medium_words_list)
    return medium_words_list

def hard_words(word_list):
    hard_words_list = []
    for word in word_list:
        if 8 <= len(word):
            hard_words_list.append(word)
    # word = random.choice(hard_words_list)
    return hard_words_list

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
    3. Performs the game loop, consisting of:
       a. Printing the word in progress, using _ for unguessed letters
       b. Printing the number of guesses remaining
       c. Printing the letters that have been guessed so far
       d. Prompting the user for a letter to guess
    4. Finishing the game and displaying whether the user has won or lost
    """
    print('\n\n\n\nThe Mystery Word Challenge')
    print("""\n\nWhat level do you want to play?\n
    1 - Easy 4-6 letters
    2 - Medium 6-8 letters
    3 - Hard 8 + letters
    4 - QUIT\n""")

    level = input("Enter a number 1-4 to start:\n")


    # word = ''
    if level is '4':
        print("\nThanks for playing the game.\n")
        exit()
    elif level is '1':
        word = random.choice(easy_words(word_list))
    elif level is '2':
        word = random.choice(medium_words(word_list))
    elif level is '3':
        word = random.choice(hard_words(word_list))

    print("\n Your word is {} letters long.\n".format(len(word)))

    chances = 8
    gameplay(chances, word)


def gameplay(chances, word):
    while chances > 0:
        guesses = []
        while True:
            if chances > 0:
                print("\n You have {} chances remaining.\n".format(chances))
                print(display_word(word, guesses))
            # if chances < 8:
            #     print("\n Letters you have already guessed: {} ".format(' '.join(guesses)))
            # elif chances > 0:

            # elif chances == 1:
            #     print("\n You have {} chance remaining.".format(chances))
            else:
                print("\n Sorry you didn't win this time")
                print("\n The word was {}. ".format(word))
                replaygame()

            guess = input("pick a letter:  ")
            if len(guess) > 1:
                print("Try picking just 1 letter")
                continue
            elif guess in guesses:
                print("I think you already played the letter {}. I won't count it against you. ".format(guess))
                continue
            else:
                guesses.append(guess)

            if guess in word:
                print("That letter is in the word!")
                if is_word_complete(word, guesses):
                    print("YOU WON!")
                    replaygame()
            else:
                print("That letter is not in the word. You will have to try again.")
                chances -= 1
            print("\n Letters you have already guessed: {} ".format(' '.join(guesses)))
            print(display_word(word, guesses))


def replaygame():
    """
    5. Giving the user the option to play again
    """
    while True:
        response = input("Do you want to play the game again?  'y' or 'n' ?")
        if response == 'y':
            main()
        else:
            print("Thanks for playing the game.")
            exit()


if __name__ == '__main__':
    main()
