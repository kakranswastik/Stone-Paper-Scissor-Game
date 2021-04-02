import random

choices = ["stone", "paper", "scissor"]
Comp = random.choice(choices)
print("""
-----------------------------------------------------------
       Welcome to the Stone, Paper and Scissor game!       
-----------------------------------------------------------\n""")

while True:
    User = input("Enter your choice {stone, paper or scissor}: ")

    if Comp == "stone" and User == "stone":
        print("Its a tie! Computer's choice: stone.\n")

    elif Comp == "stone" and User == "paper":
        print("You won! Computer's choice: stone.\n")

    elif Comp == "stone" and User == "scissor":
        print("You lost! Computer's choice: stone.\n")

    elif Comp == "paper" and User == "paper":
        print("Its a tie! Computer's choice: paper.\n")

    elif Comp == "paper" and User == "stone":
        print("You lost! Computer's choice: paper.\n")

    elif Comp == "paper" and User == "scissor":
        print("You won! Computer's choice: paper.\n")

    elif Comp == "scissor" and User == "stone":
        print("You won! Computer's choice: scissor.\n")

    elif Comp == "scissor" and User == "paper":
        print("You lost! Computer's chioce: scissor.\n")

    elif Comp == "scissor" and User == "scissor":
        print("Its a tie! Computer's choice: scissor.\n")

    elif User == "quit":
        print("Exitng game.\n")
        print("Have a nice day!\n")
        break

    else:
        print("Enter a valid value!")