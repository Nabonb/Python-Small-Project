import random
while True:
    Choice = ["rock","paper","scissor"]
    Computer = random.choice(Choice)


    Player = None

    while Player not in Choice:
        Player = input("rock , paper or scissor ?:").lower()
    if Player == Computer:
            print("This round is tie now !")
    elif Player == "rock":
        if Computer == "paper":
            print("Computer Choose : "+Computer)
            print("Player Choose : "+Player)
            print("Opps ! You Loose This Round ! :-(")
        elif Computer == "scissor":
            print("Computer Choose : " + Computer)
            print("Player Choose : " + Player)
            print("Hurrah ! You Won This Round ! :-)")
    elif Player == "paper":
        if Computer == "scissor":
            print("Computer Choose : " + Computer)
            print("Player Choose : " + Player)
            print("Opps ! You Loose This Round ! :-(")
        elif Computer == "rock":
            print("Computer Choose : " + Computer)
            print("Player Choose : " + Player)
            print("Hurrah ! You Won This Round ! :-)")
    elif Player == "scissor":
        if Computer == "rock":
            print("Computer Choose : " + Computer)
            print("Player Choose : " + Player)
            print("Opps ! You Loose This Round ! :-(")
        if Computer == "paper":
            print("Computer Choose : " + Computer)
            print("Player Choose : " + Player)
            print("Hurrah ! You Won This Round ! :-)")

    another = input("Do you want to play another round ? (yes/no)?:").lower()
    if another != "yes":
        break
print("The Game Is Over . Thanks For Playing, See You Next Time BYE ;=)")




