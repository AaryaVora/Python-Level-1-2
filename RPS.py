li = ["rock","paper","sciccor"]
import random
ComputerChoice = random.choice(li)
UserInput = input("Enter rock, paper or sciccor \n")
if UserInput ==  ComputerChoice:
    print("Its a tie!")
elif UserInput == "rock" and ComputerChoice == "sciccor":
    print("Congratulations you win!")
elif UserInput == "rock" and ComputerChoice == "paper":
    print("You lose! Better luck next time.")
# elif UserInput == "rock" and ComputerChoice == "rock":
#     print("Its a tie!")
elif UserInput == "paper" and ComputerChoice == "sciccor":
    print("You lose! Better luck next time.")
elif UserInput == "paper" and ComputerChoice == "rock":
    print("Congratulations! You win!")
# elif UserInput == "paper" and ComputerChoice == "paper":
#     print("Its a tie")
elif UserInput == "sciccor" and ComputerChoice == "rock":
    print("You lose! Better luck next time.")
elif UserInput == "sciccor" and ComputerChoice == "paper":
    print("You win! Congratulations!")
else:
    print("Please enter rock paper or sciccor.")