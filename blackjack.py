# A 2 3 4 5 6 7 8 9 10 J Q K
# ♠, ♥, ♣, ♦
# 4 * 13 = 52 장 

# blackjack rule
# 딜러에게 카드를 한장씩 받아 21에 가까운 수를 만드는 사람이 이기며 21을 초과하면 지는 게임. 
# 처음 두장 받음
# 딜러 규칙 : 16 이하면 무조건 히트, 17 이상이면 무조건 스테이

import random
import sys
pattern = ["♠", "♥", "♣", "♦"]
num = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
card_set = []

for i in pattern:
    for j in num:
        card_set.append(j+i)


def BlackJack():
    print("==============================================")
    print("===                {} {} {} {}             ===")
    print("===                                        ===")
    print("===                                        ===")
    print("==============================================")

playercard = []
dealercard = []
playercard_sum = 0
dealercard_sum = 0
dealercondition = True

def giveCard():
    card = random.choice(card_set)
    card_set.remove(card)
    return card

def change2num(card_list):
    num = []
    for i in card_list:
        if i[0] == "A":
            num.append(int(1))
        elif i[0] in ["J","Q","K"]:
            num.append(int(10))
        elif i[0:2] == "10":
            num.append(int(10))
        else:
            num.append(int(i[0]))
    return num
    
print("Game Start")
playercard.append(giveCard())
dealercard.append(giveCard())

while True:
    playercard.append(giveCard())
    if dealercondition == True:
        dealercard.append(giveCard())
    playercard_sum = sum(change2num(playercard))
    dealercard_sum = sum(change2num(dealercard))
    print("Your Cards = ",end="")
    for i in range(len(playercard)):
        print(playercard[i],end=" ")
    print("")
    print("Your Cards Sum = {}".format(playercard_sum))

    if playercard_sum > 21:
        print("You Lose //// Dealer Card {}".format(dealercard_sum))
        break
    elif dealercard_sum > 21:
        print("You Win //// Dealer Card {}".format(dealercard_sum))
    elif playercard_sum == 21:
        print("WINNER WINNER CHICKEN DINNER!")
        break
    
    if dealercard_sum > 17:
        dealercondition = False
    print("Go = 1 Stop = 2")
    choice = int(sys.stdin.readline().rstrip())
    if choice == 1:
        pass
    elif choice == 2:
        if playercard_sum > dealercard_sum:
            print("WINNER WINNER CHICKEN DINNER!")
            break
        else:
            print("You Lose //// Dealer Card {}".format(dealercard_sum))
            break
