

def play():
    isplaying = ""
    
    while isplaying !=True and isplaying != False:
        play=input("do you wish to play blackjack? (y/n)").lower()
        if play == "y":
            isplaying = True
        elif play == "n":
            isplaying = False
            print("too bad :(")
        else:
            print("Type Y or N please ")
            play=input("do you wish to play blackjack?").lower()
    return isplaying

while play() == True:
    deck=[]
    for i in range(1,53):
        deck.append(i)
        

    break