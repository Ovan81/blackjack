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
    hand=0
    def add_card(self, card):
        hand += card

   

class Card:

    def __init__(self, cardvalue):
        cardtype()
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

class Game:
    
    Deck = Deck()
    Player = Hand()
    Computer = Hand()
    Card = Card()

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

