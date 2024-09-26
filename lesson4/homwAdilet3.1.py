import random


while True:
    san = random.randint(1,100)
    print("kez-kelgen san:")
    print(san)
    user_san = int(input())
    if user_san < san:
        print("Kishi, tagy synap kor")
    elif user_san > san:
        print("Ulken, tagy synap kor")
    else:
        print("Barekeldi! dal taptyn")
        break
    
