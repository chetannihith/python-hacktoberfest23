import random

options = ("Rock","Paper","Scissors")
user = None
computer = random.choice(options).capitalize()
playing = True

while playing:
    user = None
    while user not in options:
        user=input("rock/paper/scissors??").capitalize()


    print("---------------------------------- ")

    print(f"player,s choice:{user}")
    print(f"computer's choice:{computer}")

    if computer == user:
        print("Draw")
    elif (computer=="Rock" and user=="Paper") or (computer=="Paper" and user=="Scissors") or (computer=="Scissors" and user=="Rock"): 
        print("You won!!!")
    
    else :
        print("you lose!!!")

    again = input("Want to play again??(y/n)").lower()
    if not again == "y":
        playing=False

print("Thanks for playing!!")

    
