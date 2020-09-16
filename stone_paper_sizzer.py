#My stone paper sizzer game...
import random
items=['s','p','k']
tie=0
computer_point=0
user_point=0
take_chance=0
total_chances=5
# print(user_input)

while(take_chance<total_chances):
    print("s:Stone p:Paper k:sizzer(katar)")
    computer_input=random.choice(items)
    # print("helllo")
    user_input=input("choose one from above list...")
    if user_input==computer_input:
        print("you both choose same option...")
        tie=tie+1

    #this code is for stone..
    elif user_input=="s" and computer_input=="p":
        print(f"computer choose:{computer_input}")
        print("computer got  1 point ")
        computer_point+=1
    elif user_input=="s" and computer_input=="k":
        print(f"computer choose:{computer_input}")
        print("you got one point you choose  stone..")
        user_point+=1

    #this code is for paper....
    elif user_input=="p" and computer_input=="s":
        print(f"computer choose:{computer_input}")
        print("you got one point you choose  paper..")
        user_point+=1

    elif user_input=="p" and computer_input=="k":
        print(f"computer choose{computer_input}")
        print("computer got  1 point")
        computer_point+=1

    #this code is for sizzer....
    elif user_input=="k" and computer_input=="p":
        print(f"computer choose:{computer_input}")
        print("you got one point you choose  katar(sizzer)..")
        user_point+=1

    elif user_input=="k" and computer_input=="s":
        print(f"computer choose:{computer_input}")
        print("computer got  1 point")
        computer_point+=1
    take_chance+=1

	

print(f"your points are {user_point} and computer points are {computer_point}")
print(f"{tie} times ties....")
if(user_point>computer_point):
	print("you are winner...")
else:
	print("computer is winner")
