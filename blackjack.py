import random
import time

clubs=["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "knight", "queen", "king"]
hearts=["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "knight", "queen", "king"]
spades=["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "knight", "queen", "king"]
diamonds=["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "knight", "queen", "king"]


def cardpicker():
    
    choice=(random.randint(0, len(clubs) + len(hearts) + len(spades) + len(diamonds)))
    if choice <= len(clubs):
        suit = "clubs"
    elif choice <= len(clubs) + len(hearts):
        suit = "hearts"
    elif choice <= len(clubs) + len(hearts) + len(spades):
        suit = "spades"
    else:
    suit = "diamonds"
print (cardpicker)
play=input("do you wish to play blackjack?").lower()
print(play)
while play != "true" and play != "false":
    print(play)
    if play == "yes" or play == "yea!" or play == "perchance":
        play="true"
    elif play == "no":
        play = "false"
        print("D:")
    else:
        print("TROGLODYTE UNGA BUNGA MOMENT")
        play=input("do you wish to play blackjack?").lower()
        

