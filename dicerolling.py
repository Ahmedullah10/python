
import random

def roll_dice():
    dice = random.randint(1, 6)
    print("You rolled:", dice)

def dice_simulator():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        choice = input("Do you want to roll the dice? (yes/no): ").lower()

        if choice == "yes":
            roll_dice()
        elif choice == "no":
            print("Thanks for playing!")
            break
        else:
            print("Please enter yes or no.")

dice_simulator()
