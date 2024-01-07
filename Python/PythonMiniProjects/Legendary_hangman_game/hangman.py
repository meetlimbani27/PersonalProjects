import random

def get_word():
    word_list = ["meet", "krisha"]
    return random.choice(word_list)


def display_word(word, guessed_letter):
    display_word=""
    for letter in word:
        if letter in guessed_letter:
            display_word += guessed_letter
        else:
            display_word += "_"
    print(display_word)

def hangman():
    print("Welcome to Hangman")
    word = get_word()
    guessed_letter = []
    incorrect_guess = 0
    max_incorrect_guess = 6

    
    while True:
        display_word(word, guessed_letter)
        guess = input("Enter your guess:").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input: Enter only single character")
            continue

        if guess in guessed_letter:
            print("you have already guessed that letter.")
            continue

        guessed_letter.append(guess)
        
        if guess in word:
            print("Correct guess!") 
        else:
            incorrect_guess += 1
            print("Incorrect guess!")
            print_hangman(incorrect_guess)
      
        if all(letter in guessed_letter for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

        if incorrect_guess == max_incorrect_guess:
            print("Game over! You have reached the maximum number of incorrect guesses.")
            print("The word was:", word)
            break

def print_hangman(incorrect_guesses):
    hangman = [
        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        """
    ]
    print(hangman[incorrect_guesses])


        

hangman()

