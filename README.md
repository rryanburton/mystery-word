# Mystery Word

Loads words from `/usr/share/dict/words`

## Description

In your game, you will be playing against the computer.

The computer must select a word at random from the list of words in the file /usr/share/dict/words. This file exists on your computer already.

The game must be interactive; the flow of the game should go as follows:

Let the user choose a level of difficulty at the beginning of the program.
Easy mode only has words of 4-6 characters; normal mode only has words of 6-8 characters; hard mode only has words of 8+ characters.

At the start of the game, let the user know how many letters the computer's word contains.

Ask the user to supply one guess (i.e. letter) per round.
This letter can be upper or lower case and it should not matter.

If a user enters more than one letter, tell them the input is invalid and let them try again.
Let the user know if their guess appears in the computer's word.
Display the partially guessed word, as well as letters that have not been guessed.

For example, if the word is BOMBARD and the letters guessed are a, b, and d, the screen should display:

B _ _ B A _ D

A user is allowed 8 guesses.
Remind the user of how many guesses they have left after each round.

A user loses a guess only when they guess incorrectly. If they guess a letter that is in the computer's word, they do not lose a guess.

If the user guesses the same letter twice, do not take away a guess. Instead, print a message letting them know they've already guessed that letter and ask them to try again.

The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses, reveal the word to the user when the game ends.

When a game ends, ask the user if they want to play again. The game begins again if they reply positively.



This is based off a similar exercise in MIT's 6.00.1x course.
