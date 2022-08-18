# Project : A simple Rock, Paper and scissors

import random


while True:
    options = ["rock", "paper", "scissors"]

    print("\nChoice Menu:")
    print("**********************************")
    print("-> Choose: rock, paper, or scissors")
    print("-> Press e to exit game")
    print("**********************************\n")

    # User Choice
    user_choice = input("Your Choice: ")
    user_choice.lower()

    if user_choice == "e":
        exit()

    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        print("Please choose a right answer!")
        continue

    # Computer Choice
    computer_choice = random.choice(options)
    print(f"Computer Chose: {computer_choice}")

    # Comparisons
    if user_choice == computer_choice:
        print("Match Tied!")
        print(end="\n")
        continue

    # 2*3 = 6 Conditional statements
    elif user_choice == "paper" and computer_choice == "rock":
        print("You Win!")
        break

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You Win!")
        break

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You Win!")
        break

    else:
        print("You Lose. Try Again!")
        print(end="\n")
        continue
