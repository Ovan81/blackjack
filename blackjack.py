import random
import time
base=["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "knight", "queen", "king"]

clubs=base
hearts=base
spades=base
diamonds=base
hand=0
dealerhand=0
def cardpicker():
    choice=(random.randint(0, len(clubs) + len(hearts) + len(spades) + len(diamonds)))
    if choice <= len(clubs):
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

cardlist=cardpicker()
print(cardlist)
play=input("do you wish to play blackjack?").lower()
print(play)
while play != "true" and play != "false":
    if play == "yes" or play == "yea!" or play == "perchance":
        play="true"
    elif play == "no":
        play = "false"
        print("D:")
    else:
        print("TROGLODYTE UNGA BUNGA MOMENT")
        play=input("do you wish to play blackjack?").lower()
while play == "true":
    cardlist=cardpicker()
    hand=hand + int(cardlist[0])
    print(hand)
    