import random

def roll_dice():
    """Simulates rolling a dice and returns the result."""
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    play_again = True

    while play_again:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print("The dice rolled and the result is:", result)

        play_again = input("Do you want to roll again? (y/n): ").lower() == "y"

    print("Thank you for playing the Dice Rolling Simulator!")

if __name__ == '__main__':
    main()

