import random

arr=["oppenheimer","ironman","avengers","captain_america","civi_war","thor","hulk","shaktiman","superman","wonder_women"]

x= random.choice(arr) #choice function take a string from a list

print(x)
name = input("Enter your name :- ")

chance=5

while chance>0:
    guess = input("Enter an alphabet ")
    if guess in x:
        print("-----Congratulations------")
        print("You win")
        break
    else:
        print("Try Again")
        chance-=1
if chance ==0:
    print("BETTER LUCK NEXT TIME",name)