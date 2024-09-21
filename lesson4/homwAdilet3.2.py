import random

user_ball = 0
comp_ball= 0

print("tas = k\nqaishy = n\nqagaz = b")
while True :
    user = input()
    computer = random.randint(1,3)
    if computer == 1:
        print("tas")
    elif computer == 2:
        print("qaishy")
    else:
        print("qagaz")
    if (user == 'k' and computer == 1) or (user == 'n' and computer == 2) or (user == 'b' and computer == 3):
        print("ten de ten!")
    elif (user == 'k' and computer == 2) or (user == 'n' and computer == 3) or (user == 'b' and computer == 1):
        user_ball = user_ball + 1
        print("siz zhendiniz!")
    elif (user == 'k' and computer == 3) or (user == 'n' and computer == 1) or (user == 'b' and computer == 2):
        comp_ball = comp_ball + 1
        print("siz zhenildiniz!")
    print("upaiynyz:"+ str(user_ball)+" qarsylastyn upaiy:"+str(comp_ball))
    if user_ball ==5 > comp_ball:
        print("siz uttynyz!")
        break
    elif comp_ball ==5 > user_ball:
        print("siz utyldynyz!")
        break
