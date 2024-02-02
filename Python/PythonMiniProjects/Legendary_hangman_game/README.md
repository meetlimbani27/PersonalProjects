# Hangman Game

A simple Python program that allows you to play the classic game of Hangman.

## Functionality

- Generates a random word from a predefined word list.
- Prompts the user to guess letters to reveal the hidden word.
- Displays a hangman figure as incorrect guesses are made.
- Terminates the game when the word is guessed correctly or the maximum number of incorrect guesses is reached.

## Usage

1. Run the program using Python.
2. The program will display a welcome message.
3. A random word will be selected from the predefined word list.
4. The program will display the initial state of the hidden word as underscores.
5. Enter a single letter as your guess.
6. The program will check if the guess is valid (a single character) and if it has already been guessed before.
   - If the guess is invalid or a repeated guess, the program will display an appropriate error message.
7. If the guess is valid and not repeated, the program will update the display to show the correctly guessed letters.
8. If the guess is correct, the program will display a success message.
9. If the guess is incorrect, the program will display a hangman figure and inform the user of the incorrect guess.
10. The program will continue to prompt for guesses until one of the following conditions is met:
   - The word is guessed correctly, in which case the program will display a success message.
   - The maximum number of incorrect guesses is reached, in which case the program will display a failure message and reveal the hidden word.
11. After the game ends, you can run the program again to play another round.

## Requirements

- Python 3.x

## License

Feel free to modify and use this code according to your needs.

## Author

MEET LIMBANI

## Acknowledgments

- Inspired by the desire to create a simple Hangman game.
