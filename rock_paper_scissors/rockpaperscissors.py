#I want to make Rock Paper Scissors game
import random

game_options = ["Rock", "Paper", "Scissors"]

cpu_choice = random.choice(game_options)

player_choice = input("Enter Rock, Paper, or Scissors : ")

print("CPU Choice: ", cpu_choice.lower())
print("Your Choice: ", player_choice.lower())

win = " +++++ YOU WIN +++++"
lose = " ----- YOU LOSE -----"

if player_choice.lower() == cpu_choice.lower():
    print(" YOU TIE ")
elif player_choice.lower() == "rock":
    if cpu_choice.lower() == "paper":
        print(lose)
    else:
        print(win)
elif player_choice.lower() == "paper":
    if cpu_choice.lower() == "scissors":
        print(lose)
    else:
        print(win)
elif player_choice.lower() == "scissors":
    if cpu_choice.lower() == "rock":
        print(lose)
    else:
        print(win)
else:
    print(" INVALID ENTRY ")