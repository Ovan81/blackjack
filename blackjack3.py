#blackjack-regler tas frän https://www.star.com.au/goldcoast/sites/star.com.au.goldcoast/files/Blackjack.pdf
import random
import time


class Deck:
    deck=[]
    def resetdeck(self):
        self.deck.clear()
        for i in range (1,53):
            self.deck.append(i)
    
    def shuffledeck(self):
        random.shuffle(self.deck)

class Hand:
    
    def __init__(self):
        self.hand=0

    def add_card(self, cardvalue):
        """ cardvalue 1, 2, 3, 10, 11, 12, 13"""
        hand += cardvalue

    def sum(self):
        return -1

   

class Card:

    def __init__(self, cardindex):
        """ cardindex 1, 2, ... 52 """

        if cardindex <= 13:
            self.suit= "clubs"
        elif cardindex > 13 and cardindex <= 26:
            self.suit = "diamonds"
        elif cardindex > 26 and cardindex <= 39:
            self.suit = "hearts"
        else:
            self.suit = "spades"
        print(self.suit)
    
        self.value = cardindex % 14


class Game:
    
    deck = Deck()
    player = Hand()
    computer = Hand()


    isplaying = ""
    


    def isplaying(self):
        
        play=input("do you wish to play blackjack? (y/n)").lower()
        while self.isplaying != True and self.isplaying != False:
            if play == "y":
                self.isplaying = True
            elif play == "n":
                self.isplaying = False
                print("too bad :(")
            else:
                print("Type Y or N please ")
                play=input("do you wish to play blackjack?").lower()

    def addcardtohand(self):
        tempcard = deck[0]
        Deck.deck.remove(0)
        self.hand.append(tempcard)

    def master(self):
        self.isplaying()
        while self.isplaying == True:



            self.Deck.resetdeck()
            print(Deck.deck)

            self.Deck.shuffledeck()
            print(Deck.deck)
            self.Card.cardtype(Deck.deck)
            self.Card.cardvalue(Deck.deck)
            self.Computer.addcardtohand()
            print(Computer.hand)

            break

Game = Game()
Game.master()

