import random
while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock , paper or scissors? : ").lower()
    if player == computer:
        print("computer: ", computer)
        print("Player: ", player)
        print("Tie")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("Player: ", player)
            print("You lose")
        if computer == "scissors":
            print("computer: ", computer)
            print("Player: ", player)
            print("You win")
    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("Player: ", player)
            print("You win")
        if computer == "scissors":
            print("computer: ", computer)
            print("Player: ", player)
            print("You lose")
    elif player == "scissors":
        if computer == "paper":
            print("computer: ", computer)
            print("Player: ", player)
            print("You win")
        if computer == "rock":
            print("computer: ", computer)
            print("Player: ", player)
            print("You lose")
    play_again = input("would u like to play again?  y/n?").lower()

    if play_again != 'y':
        break
print("bye")