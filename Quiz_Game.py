print("Hello Welcome To The Gamers World !!")
playing = input("Do you want to play this game ? ").lower()
score = 0

if playing!= "yes":
    print("Thank you for came here")
    quit()

print("Oke !! Let's play this game")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Hurreh ! You are correct :)")
    score +=1
else:
    print("Sorry your answer is wrong :(")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Hurreh ! You are correct :)")
    score += 1
else:
    print("Sorry your answer is wrong :(")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Hurreh ! You are correct :)")
    score += 1
else:
    print("Sorry your answer is wrong :(")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print("Hurreh ! You are correct :)")
    score += 1
else:
    print("Sorry your answer is wrong :(")
print("You Made "+str(score)+" score out of 4")
print("Your Achived "+str((score/4)*100)+"%.")
print("The Game Is Over Thank You for Your Perticipation !! BYE")
