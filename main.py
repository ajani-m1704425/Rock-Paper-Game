import random


Available_choice = ["R", "P", "S"]


def Player_init():
    value = input("Pick an option between \"R\", \"P\" or \"S\": ")
    value = value.upper()
    while value not in Available_choice:
        print("\nNot amongst our options\n")
        value = input("Pick an option between \"R\", \"P\" or \"S\": ")
        value = value.upper()
    return value


def Game_init():
    Player_choice = Player_init()
    Computer_choice = random.choice(Available_choice)
    if Player_choice == "R" and Computer_choice == "P":
        print("Player(Rock) : CPU(Paper)\n")
        print("CPU Wins")
        return "CPU"
    elif Player_choice == "P" and Computer_choice == "S":
        print("Player(Paper) : CPU(Scissors)\n")
        print("CPU Wins")
        return "CPU"
    elif Player_choice == "S" and Computer_choice == "R":
        print("Player(Scissors) : CPU(Rock)\n")
        print("CPU Wins")
        return "CPU"
    elif Player_choice == "P" and Computer_choice == "R":
        print("Player(Paper) : CPU(Rock)\n")
        print("Player Wins")
        return "Player"
    elif Player_choice == "S" and Computer_choice == "P":
        print("Player(Scissors) : CPU(Paper)\n")
        print("Player Wins")
        return "Player"
    elif Player_choice == "R" and Computer_choice == "S":
        print("Player(Rock) : CPU(Scissors)\n")
        print("Player Wins")
        return "Player"
    elif Player_choice == "P" and Computer_choice == "P":
        print("Player(Paper) : CPU(Paper)\n")
        print("It's a tie")
        return "Tie"
    elif Player_choice == "R" and Computer_choice == "R":
        print("Player(Rock) : CPU(Rock)\n")
        print("It's a tie")
        return "Tie"
    elif Player_choice == "S" and Computer_choice == "S":
        print("Player(Scissors) : CPU(Scissors)\n")
        print("It's a tie")
        return "Tie"


Outcome = Game_init()

while Outcome == "Tie":
    Outcome = Game_init()
