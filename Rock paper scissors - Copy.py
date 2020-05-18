import random
Objects=["Rock","Paper","Scissors"]
bot1=random.randint(1,len(Objects)-1)
bot2=Objects[bot1]

print("Wanna play rock paper scissors. Loser has to die")
choice=input()
if choice=="Rock":
    print("You have chose Rock.")
elif choice=="Paper":
    print("You have chose Paper.")
elif choice=="Scissors":
    print("You have chose Scissors.")
print("Who asked")
print("I have chose")
print(bot2)
if choice==bot2:
    print("Hey stop it copy cat.")
if choice=="Rock":
    if bot2=="Paper":
        print("Well I guess I have to die now")
if choice=="Paper":
    if bot2=="Scissors":
        print("Well I guess I have to die now")
if choice=="Scissors":
    if bot2=="Rock":
        print("Well I guess I have to die now")
if choice=="Paper":
    if bot2=="Rock":
        print("Well I guess I have to die now")
if choice=="Scissors":
    if bot2=="Paper":
        print("Well I guess I have to die now")
if choice=="Rock":
    if bot2=="Scissors":
        print("Well I guess I have to die now")



