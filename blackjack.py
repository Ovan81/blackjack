#blackjack-regler tas frän https://www.star.com.au/goldcoast/sites/star.com.au.goldcoast/files/Blackjack.pdf
import random
import time



class rules:

    base=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    clubs=base
    hearts=base
    spades=base
    diamonds=base
    play=False

    def isplaying(self):
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

    def cardpicker(self):
        deck = clubs + hearts + spades + diamonds
        print(deck)
        choice = (random.randint(0, len(deck)))
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
        cardlist = [choice, suit, deck]
        return cardlist
        
    def cardtype(self, i):
        cardlist = cardpicker()
       
        print(cardlist)
        if cardlist[0] == 1:
            print("you got ace of", cardlist[1])
        elif cardlist[0] == 11:
            print("you got knight of", cardlist[1])
        elif cardlist[0] ==12:
            print("you got queen of", cardlist[1])
        elif cardlist[0] == 13:
            print("you got king of", cardlist[1])
        else:   
            print("you got", cardlist[0], "of", cardlist[1])
        




class dealer: 
    hand=0
    def addcardtohand(self, cardlist):
        hand=hand + cardlist[0]

class player:
    hand=0
    def addcardtohand(self, cardlist):

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

rules.isplaying()

while rules.play == True:
    for i in range (playercount):
      addcardtohand()

    break
    