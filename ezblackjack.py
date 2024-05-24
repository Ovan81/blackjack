#blackjack-regler tas frän https://www.star.com.au/goldcoast/sites/star.com.au.goldcoast/files/Blackjack.pdf, men ändringar i reglerna kan ske.
import random
import time
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
            time.sleep(1)
            print("too bad :(")
        else:
            print("type y or n please")
    return isplaying
    
def cardsuit():
    if deck[0] <= 13:
        suit= "clubs"
    elif deck[0] > 13 and deck[0] <= 26:
        suit = "diamonds"
    elif deck[0] > 26 and deck[0] <= 39:
        suit = "hearts"
    else:
        suit = "spades"

    return suit


    

def addcardtohand(deck, hand):
    tempcard = deck[0]
    deck.pop(0)
    hand.append(tempcard)

    if  hand[-1] <= 13:
        None
    elif hand[-1] > 13 and hand[-1] <= 26:
        hand[-1] -= 13
    elif hand[-1] > 26 and hand[-1] <= 39:
        hand[-1] -= 26
    else:
        hand[-1] -= 39



    if hand[-1] == 11:
        hand[-1]=10
        presentingvalue="knight"
    elif hand[-1] == 12:
        hand[-1]=10
        presentingvalue="queen"
    elif hand[-1] == 13:
        hand[-1]=10
        presentingvalue="king"
    elif hand[-1]==1:
        hand[-1]=11
        presentingvalue="ace"
    else:
        presentingvalue=hand[-1]

    return presentingvalue
    

def hitorstand():
    action=None
    while action != "h" and action != "s":
        action=input("hit or stand? (h/s)").lower()
        time.sleep(1)
        if action == "h":
            cardtype=cardsuit()
            cardvalue=addcardtohand(deck, playerhand)
            print("you got", cardvalue, "of", cardtype + "!")
            time.sleep(1)
            
            action=None
            if sum(playerhand) > 21 and 11 in playerhand:
                playerhand[playerhand.index(11)]=1
            elif sum(playerhand) >21:
                action="s"
            print("your card total is now", sum(playerhand))
            time.sleep(1)
        elif action == "s":
            time.sleep(1)
        else:
            print("wrong input!")


def computerhit():
    while sum(computerhand) <= 16:
        cardtype=cardsuit()
        cardvalue=addcardtohand(deck, computerhand)
        if sum(playerhand) > 21 and 11 in playerhand:
                playerhand[playerhand.index(11)]=1

while play(question) == True:
    deck.clear()
    playerhand.clear()
    computerhand.clear()
    for i in range(1,53):
        deck.append(i)
    random.shuffle(deck)
    time.sleep(1)

    cardtype=cardsuit()
    cardvalue=addcardtohand(deck, playerhand)
    print("you got", cardvalue, "of", cardtype + "!")
    time.sleep(1)

    cardtype=cardsuit()
    cardvalue=addcardtohand(deck, computerhand)
    print("The dealer got", cardvalue, "of", cardtype + "!")
    time.sleep(1)

    cardtype=cardsuit()
    cardvalue=addcardtohand(deck, playerhand)
    print("you got", cardvalue, "of", cardtype + "!")
    time.sleep(1)

    cardtype=cardsuit()
    cardvalue=addcardtohand(deck, computerhand)
    print("The dealer got dealt a second card!")
    time.sleep(1)

    print("your card total is now", sum(playerhand))
    time.sleep(1)

    hitorstand()
    computerhit()




    
    if sum(playerhand) > 21:
        print ("You went busto, the dealer wins!") 
    elif sum(computerhand) > 21:
        print ("The dealer went Busto, you win!")
    elif sum(playerhand) > sum(computerhand):
        print ("you won!")
    elif sum(playerhand) < sum(computerhand):
        print ("the the dealer won!")
    else:
        print ("It's a tie!")
    time.sleep(1)


    question = ("do you want to play again? (y/n)")
    

    