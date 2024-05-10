#blackjack-regler tas frän https://www.star.com.au/goldcoast/sites/star.com.au.goldcoast/files/Blackjack.pdf, men ändringar i reglerna kan ske.
import random
question = "do you want to play? (y/n)"
playerhand=[]
computerhand=[]
deck=[]

def play(question):
    isplaying = ""
    
    while isplaying !=True and isplaying != False:
        play=input(question).lower()
        if play == "y":
            isplaying = True
        elif play == "n":
            isplaying = False
            print("too bad :(")
        else:
            play=input("type y or n, please.").lower()
    return isplaying

def cardsuit(card):
    if card <= 13:
        suit= "clubs"
    elif card > 13 and card <= 26:
        suit = "diamonds"
    elif card > 26 and card <= 39:
        suit = "hearts"
    else:
        suit = "spades"

    return suit

def cardindex (card): 
    cardvalue=card
    if cardvalue <= 13:
        None
    elif cardvalue >= 13 and cardvalue < 26:
        cardvalue -= 13
    elif cardvalue >= 26 and cardvalue < 39:
        cardvalue -= 26
    else:
        cardvalue -= 39

    if cardvalue == 1:
        cardvalue ="ace"
    elif cardvalue == 11:
        cardvalue = "knight"
    elif cardvalue == 12:
        cardvalue = "queen"
    elif cardvalue == 13:
        cardvalue = "king"
    else:
        None
    return cardvalue
    
    

def addcardtohand(deck, hand):
        tempcard = deck[0]
        deck.pop(0)
        hand.append(tempcard)


while play(question) == True:
    deck.clear
    for i in range(1,53):
        deck.append(i)
    random.shuffle(deck)
        


    addcardtohand(deck, playerhand)
    cardtype=cardsuit(playerhand[-1])
    cardvalue=cardindex(playerhand[-1])
    print("you got", cardvalue, "of", cardtype + "!")

    addcardtohand(deck, computerhand)
    cardtype=cardsuit(computerhand[-1])
    cardvalue=cardindex(computerhand[-1])
    print("The dealer got", cardvalue, "of", cardtype + "!")

    addcardtohand(deck, playerhand)
    cardtype=cardsuit(playerhand[-1])
    cardvalue=cardindex(playerhand[-1])
    print("you got", cardvalue, "of", cardtype + "!")
    

   

    question = ("do you want to play again? (y/n)")
    

    