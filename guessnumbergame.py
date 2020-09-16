import random
num = random.randint(1, 50)
print(num)
print("how many chance do you want to solve this guessing game...")
chance=int(input())
takechance=0
while(takechance<chance):
    guess = int(input("enter the number"))
    if (guess > num):
        print("you choose a high number")
        # takechance=takechance+1
    elif(guess < num):
        print("you choose a lower number")
        # takechance=takechance+1
    else:
        print(f"you took {takechance+1} chance,to  correct guess")
        break
    takechance=takechance+1
print("game is over")