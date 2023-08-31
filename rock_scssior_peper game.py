
# ********************* algorithm ***************************
# create list contain rock,scissor,peper
# create varible p1,p2,p1_point=0,p2_point=0,time=6
# p1 receive a string entered by user and check if its in list
# p2 store a random value of the list
# check if the priority of p1 higher than p2 will add 1 point to p1_point
# else if p2 has priority more than p1 we will add 1 point to p2_point else 1 point for p1_point,p2_point
# this game will be repated 6 times
# if p1_point has more point show message he win else he lost else the result is draw
#

import random
time = 6
p1_point=0
p2_point=0
word = ["rock","scissor","peper"]
while time>0:
    p1=input("Choose one of them to start playing\n1- rock\n2- scissor\n3- peper\n")
    while p1 not in word:
        p1 = input("Your choice should be one of them to start playing\n1- rock\n2- scissor\n3- peper\n")
    p2=random.choice(word)
    if p1 == "rock" and p2 == "scissor": p1_point +=1
    elif p1 == "rock" and p2 == "peper": p2_point +=1
    elif p1 == "peper" and p2 == "rock": p1_point +=1
    elif p1 == "peper" and p2 == "scissor": p2_point +=1
    elif p1 == "scissor" and p2 == "peper": p1_point +=1
    elif p1 == "scissor" and p2 == "rock": p2_point +=1
    else:
        p1_point +=1
        p2_point +=1
    time -=1

if p1_point>p2_point:
    print("You win!!")
elif p1_point<p2_point:
    print("You lost!!")
else:print("The result is draw")

print(f"Your points is: {p1_point}")
print(f"computer points is: {p2_point}")