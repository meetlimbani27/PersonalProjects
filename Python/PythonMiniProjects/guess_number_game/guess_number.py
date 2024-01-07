import random

gnum = random.randint(1 , 100)
attempts = 0

while True:
    inum =input("Enter your guess between 1 to 100: ").strip()
    attempts += 1
    if inum.isdigit():
        inum = int(inum)
        if 1 <= inum <= 100:
            if inum < gnum:
                print("guess higher")
            elif inum > gnum:
                print("guess lower")
            else:
                break
        else:
            print("Invalid Input, please enter a number between 1 to 100")
    else:
        print("Invalid Input, please enter a number between 1 to 100")

if inum == gnum:
    print(f"Bingo, Got that right in {attempts} attempts")
