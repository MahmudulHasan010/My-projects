import random
while 1==1:
    choices=["rock","paper","scissor"]
    computer=random.choice(choices)
    player=None
    while player not in choices:
        player=input("Choose rock, paper or scissor :")
    print("computer chose :",computer)
    print("player chose :",player)
    if player==computer:
        print("It's a tie")
    if player=="rock":
        if computer=="scissor":
            print("You Win")
        elif computer=="paper":
            print("You Lose")
    if player=="paper":
        if computer=="rock":
            print("You Win")
        elif computer=="scissor":
            print("You Lose")
    if player=="scissor":
        if computer=="paper":
            print("You Win")
        elif computer=="rock":
            print("You Lose")
    play=input("Do you want to play again?(YES/Any key)")
    play=play.upper()
    if play!="YES":
        break
print("Thanks for playing!")




