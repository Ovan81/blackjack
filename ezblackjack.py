isplaying=""


def play(self):
    play=input("do you wish to play blackjack? (y/n)").lower()
    while isplaying !=True and isplaying != False:
        if play == "y":
            isplaying = True
        elif play == "n":
            isplaying = False
            print("too bad :(")
        else:
            print("Type Y or N please ")
            play=input("do you wish to play blackjack?").lower()

while isplaying == True:
    deck=[]
    for i in range(1,53):
        deck.append(i)
        


    break