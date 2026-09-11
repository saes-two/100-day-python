import random
list = ["Rock", "Paper", "Scissors"]
poin = 0
computer = random.choice(list)
player = len(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player >=3 or < 0:
    print("You typed an invalid number. You Lose!")
elif list[player] == "Rock" and computer == "Paper":
    print(f"Player: {list[player]}\nComputer: {computer}\nYou Lose!")
elif list[player] == "Paper" and computer == "Scissors":
    print(f"Player: {list[player]}\nComputer: {computer}\nYou Lose!")
elif list[player] == "Scissors" and computer == "Rock":
    print(f"Player: {list[player]}\nComputer: {computer}\nYou Lose!")
elif list[player] == computer:
    print(f"Player: {list[player]}\nComputer: {computer}\nDraw!")
else:
    print(f"Player: {list[player]}\nComputer: {computer}\nYou Wins!")
    
