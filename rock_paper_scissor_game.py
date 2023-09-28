import random

def game(user,com):
    if user == com:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if com == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "paper":
        if com == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user == "scissors":
        if com == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

def main():
    x=["rock","paper",'scissor']

    com = random.choice(x)

    human = int(input("1 = Rock , 2= Paper , 3= Scissors  "))

    if human == 1:
        user = "rock"
        game(user,com)
    elif human == 2:
        user = "paper"
        game(user,com)
    elif human == 3:
        user = "scissors"
        game(user,com)
    else:
        print("ENTER A VALID VALUE")

    try_again = input("If you try again Enter Y or N for exit ")
    if try_again=="Y":
        main()
main()