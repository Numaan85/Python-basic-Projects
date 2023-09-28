import random #This is random library that generate random number

x= random.randint(1,10) #randint is a function that set range of function

print("    -----Welcome To Game ------    ")

print("You have only 3 Guesses")



count =0
while count<3:
    guess= int(input("Enter a Number from 1 to 10 "))
    print(x)
    if guess == x:
        print("   ------Congratulation You won-------- ")
        print("Computer Number =",x)
        print("Your Number is",guess)
        break
    elif guess<x:
        print("Your Number is small")
        print("Try Again")
        count+=1
    elif guess>x:
        print("Your Number is too large")
        print("Try Again")
        count+=1
if count==3:
    print("")
    print("BETTER LUCK NEXT TIME")