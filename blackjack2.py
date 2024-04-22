#blackjack-regler tas frän https://www.star.com.au/goldcoast/sites/star.com.au.goldcoast/files/Blackjack.pdf
import random
import time

class Game:
    keepgoing = ""

    def isplaying(self):
        
        play=input("do you wish to play blackjack? (y/n)").lower()
        while self.keepgoing != True and self.keepgoing != False:
            if play == "y":
                self.keepgoing = True
            elif play == "n":
                self.keepgoing = False
                print("too bad :(")
            else:
                print("Type Y or N please ")
                play=input("do you wish to play blackjack?").lower()
class Deck:
    deck=[]
    def resetdeck(self):
        self.deck.clear()
        for i in range (1,53):
            self.deck.append(i)
    
    def shuffledeck(self):
        random.shuffle(self.deck)

class Hand:
    computerhand = 0
    playerhand = 0
class Card:
    suit = ""
    def cardtype(self,deck):
        if deck[0] <= 13:
            self.suit= "clubs"
        elif deck[0] > 13 and deck[0] <= 26:
            self.suit = "diamonds"
        elif deck[0] > 26 and deck[0] <= 39:
            self.suit = "hearts"
        else:
            self.suit = "spades"
        print(self.suit)
    
    def cardvalue(self, deck): 
        if deck[0] <= 13:
            None
        elif deck[0] >= 13 and deck[0] < 26:
            deck[0] -= 13
        elif deck[0] >= 26 and deck[0] < 39:
            deck[0] -= 26
        else:
            deck[0] -= 39
        print(deck[0])

Game = Game()
Deck = Deck()
Hand = Hand()
Card = Card()

Game.isplaying()
while Game.keepgoing == True:
    
    Deck.resetdeck()
    print(Deck.deck)

    Deck.shuffledeck()
    print(Deck.deck)
    Card.cardtype(Deck.deck)
    Card.cardvalue(Deck.deck)

    break

tempcard = deck[0]
deck.remove(0)
hand.append(tempcard)