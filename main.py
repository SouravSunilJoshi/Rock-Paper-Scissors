import random
# Rock paper scissors
option = ["rock","paper","scissors"]


def game(inputopt):
    print("\n You selected {} \n".format(option[inputopt]))
    x = random.randint(0,2)
    print("Computer Selected {} \n".format(option[x]))

    if (option[inputopt]== "paper" and option[x]=="paper"):
        print("Game is Tie")

    elif (option[inputopt]== "paper" and option[x]=="rock"):
        print("Player win the game")

    elif (option[inputopt]== "paper" and option[x]=="scissors"):
        print("Computer win the game")

    elif (option[inputopt]== "rock" and option[x]=="paper"):
        print("Computer win the game")

    elif (option[inputopt]== "rock" and option[x]=="rock"):
        print("Game is Tie")

    elif (option[inputopt]== "rock" and option[x]=="scissors"):
        print("Player win the game")

    elif (option[inputopt]== "scissors" and option[x]=="paper"):
        print("Player win the game")

    elif (option[inputopt]== "scissors" and option[x]=="rock"):
        print("Computer win the game")

    elif (option[inputopt]== "scissors" and option[x]=="scissors"):
        print("Game is Tie")


if __name__ == "__main__":
    print("Welcome to game")
    while True:
        try:
            inputopt = int(input("1.Rock\n2.paper\n3.scissors\nSelect Option:"))
            game(inputopt)
        except:
            print("Something went wrong")
        if input("enter y to exit:") == "y":
            break