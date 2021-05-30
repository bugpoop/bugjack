import cards
from random import randrange

global sym
global lol
global symuser
global loluser
global symhidden
global lolhidden
global symuser2
global loluser2
global symuser3
global loluser3
global valued
global valuedh

global valueu2
global valueu
global valueu3
valueu3 = 0

while True:
    print("Hi and welcome to bugjack.")
    print("Generating card values...")
    print("----------The dealers cards are----------")

    def deal():
        global valued
        face = randrange(13)
        if face == 0:
            face = 2
            valued = face
        if face == 1:
            face = 'Ace'
            valued = 1
        elif face < 11:
            face = str(face)
            valued = int(face)
       # print(face)

        if face == 11:
            face = 'Jack'
            valued = 10
        if face == 12:
            face = 'Queen'
            valued = 10
        if face == 13:
            face = 'King'
            valued = 10

        symbol = randrange(4)
        if symbol == 0:
            symbol = 1
        if symbol == 1:
            print(cards.ascii_version_of_card(cards.Card('Spades', face)))
        elif symbol == 2:
            print(cards.ascii_version_of_card(cards.Card('Diamonds', face)))
        elif symbol == 3:
            print(cards.ascii_version_of_card(cards.Card('Hearts', face)))
        elif symbol == 4:
            print(cards.ascii_version_of_card(cards.Card('Clubs', face)))
        global sym
        global lol
        if face == 11 or face == 12 or face == 13:
            lol = 10
        else:
            lol = face
        sym = symbol


    def dealhidden():
        global valuedh
        face = randrange(13)
        if int(face) > 10:
            valuedh = 10
        if face == 0:
            face = 2
            valuedh = 2
        if face == 1:
            face = 'Ace'
            valuedh = 1
        elif face < 11:
            face = str(face)
            valuedh = int(face)
    #    print(face)

        if face == 11:
            face = 'Jack'
        if face == 12:
            face = 'Queen'
        if face == 13:
            face = 'King'

        symbol = randrange(4)
        if symbol == 0:
            symbol = 1
        if symbol == 1:
            print(cards.ascii_version_of_hidden_card(cards.Card('Spades', face)))
        elif symbol == 2:
            print(cards.ascii_version_of_hidden_card(cards.Card('Diamonds', face)))
        elif symbol == 3:
            print(cards.ascii_version_of_hidden_card(cards.Card('Hearts', face)))
        elif symbol == 4:
            print(cards.ascii_version_of_hidden_card(cards.Card('Clubs', face)))
        global symhidden
        symhidden = symbol
        global lolhidden
        if face == 11 or face == 12 or face == 13:
            lolhidden = 10
        else:
            lolhidden = face
    def userdeal2():
        global valueu2
        face = randrange(13)
        if int(face) > 10:
            valueu2 = 10
        if face == 0:
            face = 2
            valueu2 = 2
        if face == 1:
            face = 'Ace'
            valueu2 = 1

        elif face < 11:
            valueu2 = int(face)
            face = str(face)
        # print(face)

        if face == 11:
            face = 'Jack'
        if face == 12:
            face = 'Queen'
        if face == 13:
            face = 'King'

        symbol = randrange(4)
        if symbol == 0:
            symbol = 1
        if symbol == 1:
            print(cards.ascii_version_of_card(cards.Card('Spades', face)))
        elif symbol == 2:
            print(cards.ascii_version_of_card(cards.Card('Diamonds', face)))
        elif symbol == 3:
            print(cards.ascii_version_of_card(cards.Card('Hearts', face)))
        elif symbol == 4:
            print(cards.ascii_version_of_card(cards.Card('Clubs', face)))
        global loluser2
        global symuser2
        if face == 11 or face == 12 or face == 13:
            loluser2 = 10
        else:
            loluser2 = face
        symuser2 = symbol

    def userdeal():
        global valueu
        face = randrange(13)
        if face > 10:
            valueu = 10
        if face == 0:
            valueu = 2
            face = 2
        if face == 1:
            valueu = 1
            face = 'Ace'

        elif face < 11:
            valueu = int(face)
            face = str(face)
            # print(face)

        if face == 11:
            face = 'Jack'
        if face == 12:
            face = 'Queen'
        if face == 13:
            face = 'King'

        symbol = randrange(4)
        if symbol == 0:
            symbol = 1
        if symbol == 1:
            print(cards.ascii_version_of_card(cards.Card('Spades', face)))
        elif symbol == 2:
            print(cards.ascii_version_of_card(cards.Card('Diamonds', face)))
        elif symbol == 3:
            print(cards.ascii_version_of_card(cards.Card('Hearts', face)))
        elif symbol == 4:
            print(cards.ascii_version_of_card(cards.Card('Clubs', face)))
        global loluser
        global symuser
        if face == 11 or face == 12 or face == 13:
            loluser = 10
        else:
            loluser = face
        symuser = symbol
    def userdeal3():
        global valueu3
        face = randrange(13)
        if face > 10:
            valueu3 = 10
        if face == 0:
            face = 2
            valueu3 = 2
        if face == 1:
            valueu3 = 1
            face = 'Ace'

        elif face < 11:
            valueu3 = int(face)
            face = str(face)
            # print(face)

        if face == 11:
            face = 'Jack'
        if face == 12:
            face = 'Queen'
        if face == 13:
            face = 'King'

        symbol = randrange(4)
        if symbol == 0:
            symbol = 1
        if symbol == 1:
            print(cards.ascii_version_of_card(cards.Card('Spades', face)))
        elif symbol == 2:
            print(cards.ascii_version_of_card(cards.Card('Diamonds', face)))
        elif symbol == 3:
            print(cards.ascii_version_of_card(cards.Card('Hearts', face)))
        elif symbol == 4:
            print(cards.ascii_version_of_card(cards.Card('Clubs', face)))
        global loluser3
        global symuser3
        if face == 11 or face == 12 or face == 13:
            loluser3 = 10
        else:
            loluser3 = face
        symuser3 = symbol


    deal()
    dealhidden()
    print("----------Your Cards are----------")
    userdeal()
    userdeal2()
    a = str(input("Would you like to double down? y/n"))
    if a == "y":
        userdeal3()
        print("----------The dealers cards are----------")
        if sym == 0:
            sym = 1
        if sym == 1:
            print(cards.ascii_version_of_card(cards.Card('Spades', lol)))
        elif sym == 2:
            print(cards.ascii_version_of_card(cards.Card('Diamonds', lol)))
        elif sym == 3:
            print(cards.ascii_version_of_card(cards.Card('Hearts', lol)))
        elif sym == 4:
            print(cards.ascii_version_of_card(cards.Card('Clubs', lol)))
        symbol = symhidden
        face = lolhidden
        if symbol == 0:
            symbol = 1
        if symbol == 1:
            print(cards.ascii_version_of_card(cards.Card('Spades', face)))
        elif symbol == 2:
            print(cards.ascii_version_of_card(cards.Card('Diamonds', face)))
        elif symbol == 3:
            print(cards.ascii_version_of_card(cards.Card('Hearts', face)))
        elif symbol == 4:
            print(cards.ascii_version_of_card(cards.Card('Clubs', face)))
        print("----------Your Cards are----------")
        symbol = symuser
        face = loluser
        if symbol == 0:
            symbol = 1
        if symbol == 1:
            print(cards.ascii_version_of_card(cards.Card('Spades', face)))
        elif symbol == 2:
            print(cards.ascii_version_of_card(cards.Card('Diamonds', face)))
        elif symbol == 3:
            print(cards.ascii_version_of_card(cards.Card('Hearts', face)))
        elif symbol == 4:
            print(cards.ascii_version_of_card(cards.Card('Clubs', face)))
        symbol = symuser2
        face = loluser2
        if symbol == 0:
            symbol = 1
        if symbol == 1:
            print(cards.ascii_version_of_card(cards.Card('Spades', face)))
        elif symbol == 2:
            print(cards.ascii_version_of_card(cards.Card('Diamonds', face)))
        elif symbol == 3:
            print(cards.ascii_version_of_card(cards.Card('Hearts', face)))
        elif symbol == 4:
            print(cards.ascii_version_of_card(cards.Card('Clubs', face)))
        symbol = symuser3
        face = loluser3
        if symbol == 0:
            symbol = 1
        if symbol == 1:
            print(cards.ascii_version_of_card(cards.Card('Spades', face)))
        elif symbol == 2:
            print(cards.ascii_version_of_card(cards.Card('Diamonds', face)))
        elif symbol == 3:
            print(cards.ascii_version_of_card(cards.Card('Hearts', face)))
        elif symbol == 4:
            print(cards.ascii_version_of_card(cards.Card('Clubs', face)))
        usertotal = valueu + valueu2 + valueu3
        dealertotal = valued + valuedh
        if dealertotal < 22 and usertotal < dealertotal:
            print("the dealer has won!")
            str(input("wanna go again?"))
        elif usertotal < 22 and usertotal > dealertotal:
            print("you won!")
            str(input("wanna go again?"))
        elif usertotal > 21:
            print("the dealer has won!")
            str(input("wanna go again?"))









    else:
        print("----------The dealers cards are----------")
        if sym == 0:
            sym = 1
        if sym == 1:
            print(cards.ascii_version_of_card(cards.Card('Spades', lol)))
        elif sym == 2:
            print(cards.ascii_version_of_card(cards.Card('Diamonds', lol)))
        elif sym == 3:
            print(cards.ascii_version_of_card(cards.Card('Hearts', lol)))
        elif sym == 4:
            print(cards.ascii_version_of_card(cards.Card('Clubs', lol)))
        symbol = symhidden
        face = lolhidden
        if symbol == 0:
            symbol = 1
        if symbol == 1:
            print(cards.ascii_version_of_card(cards.Card('Spades', face)))
        elif symbol == 2:
            print(cards.ascii_version_of_card(cards.Card('Diamonds', face)))
        elif symbol == 3:
            print(cards.ascii_version_of_card(cards.Card('Hearts', face)))
        elif symbol == 4:
            print(cards.ascii_version_of_card(cards.Card('Clubs', face)))
        print("----------Your Cards are----------")
        symbol = symuser
        face = loluser
        if symbol == 0:
            symbol = 1
        if symbol == 1:
            print(cards.ascii_version_of_card(cards.Card('Spades', face)))
        elif symbol == 2:
            print(cards.ascii_version_of_card(cards.Card('Diamonds', face)))
        elif symbol == 3:
            print(cards.ascii_version_of_card(cards.Card('Hearts', face)))
        elif symbol == 4:
            print(cards.ascii_version_of_card(cards.Card('Clubs', face)))
        symbol = symuser2
        face = loluser2
        if symbol == 0:
            symbol = 1
        if symbol == 1:
            print(cards.ascii_version_of_card(cards.Card('Spades', face)))
        elif symbol == 2:
            print(cards.ascii_version_of_card(cards.Card('Diamonds', face)))
        elif symbol == 3:
            print(cards.ascii_version_of_card(cards.Card('Hearts', face)))
        elif symbol == 4:
            print(cards.ascii_version_of_card(cards.Card('Clubs', face)))
        usertotal = valueu + valueu2 + valueu3
        dealertotal = valued + valuedh
        if dealertotal < 22 and usertotal < dealertotal:
            print("the dealer has won!")
            str(input("wanna go again?"))
        elif usertotal < 22 and usertotal > dealertotal:
            print("you won!")
            str(input("wanna go again?"))
        elif usertotal > 21:
            print("the dealer has won!")
            str(input("wanna go again?"))

