import random
comp_san = 0
user_inp = 0

while user_inp != '!':
    user_inp = input()
    if user_inp == '':
        comp_san = random.randint(1,6)
        print(user_inp, comp_san)
    
print("oiyn toqtatyldy!")
