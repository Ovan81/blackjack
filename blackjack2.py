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
    Hand=[]
class Card:
    None

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

    break

