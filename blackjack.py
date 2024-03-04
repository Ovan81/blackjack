#blackjack-regler tas frän https://www.star.com.au/goldcoast/sites/star.com.au.goldcoast/files/Blackjack.pdf
import random
import time


ace=1
knight=10
queen=10
king=10
base=[ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, knight, queen, king]
clubs=base
hearts=base
spades=base
diamonds=base

class rules:
    def cardpicker(self):
        choice=(random.randint(0, len(clubs) + len(hearts) + len(spades) + len(diamonds)))
        if choice <= len(clubs) :
            suit = "clubs"
            choice = clubs.pop(choice - 1)
        elif choice <= len(clubs) + len(hearts):
            suit = "hearts"
            choice = hearts.pop(choice - len(clubs) - 1)
        elif choice <= len(clubs) + len(hearts) + len(spades):
            suit = "spades"
            choice = spades.pop(choice - len(hearts) - len(clubs) - 1)
        else:
            suit = "diamonds"
            choice = diamonds.pop(choice - len(hearts) - len(spades) - len(clubs) - 1)
        cardlist = [choice, suit]
        return cardlist

class dealer:
    hand=0


class player:
    hand=0

players = []
playercount = input("how many will play? ")
print(playercount)
while not playercount.isdigit():
    playercount = input("wrong input, type in numbers only please!")
playercount = int(playercount)
for i in range(playercount):
    players.append(player())
print(len(players))


rules=rules()
dealer= dealer()

play=input("do you wish to play blackjack?").lower()
while play != True and play != False:
    if play == "yes" or play == "yea!" or play == "perchance":
        play= True
    elif play == "no":
         play = False
         print("D:")
    else:
        print("TROGLODYTE UNGA BUNGA MOMENT")
        play=input("do you wish to play blackjack?").lower()
        
while play == True:
    for i in range (playercount):
        cardlist = rules.cardpicker()
        players[i].hand = players[i].hand + cardlist[0]
        print(cardlist)
        print("you got", cardlist[0], "of", cardlist[1])

    cardlist = rules.cardpicker()
    dealer.hand = dealer.hand + rules.cardpicker()
    print(dealer.hand)





    break
    