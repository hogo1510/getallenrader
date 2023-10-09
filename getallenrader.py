import random
def vraag():
    vraag = str(input("Kies: b(bot) p(player): "))

    hoogte = str(input("hoe hoog mag het getal maximum zijn?: "))
    pogingQ = input("met een vast gesteld hoeveelheid pogingen? y(yes) n(no=oneindig): ")

    pogingSet = None

    if pogingQ == "y":
        pogingSet = True
        hvlpogingen = int(input("Hoeveel pogingen ?: "))
    elif pogingQ == "n":
        hvlpogingen = None
        pogingSet = False
    else:
        print(pogingQ +" Word niet herkend, kies opniew")
        #Main Settings above
        #specific Setting under
    HoogteInt = int(hoogte)
    if vraag == "b":
        print("tegen een bot")    
        antw = random.randint(0,HoogteInt)
        game_bot(antw, pogingSet, hvlpogingen)

    elif vraag == "p":
        naam = input("kies de naam voor player 2: ")
        getal = int(input(naam +" kies een getal tussen de 0 en " +hoogte +" :"))
        while getal > HoogteInt:
            getal = int(input("dit getal overschreid de maximum hoogte, gies een nieuw getal tussen de 0 en " +hoogte +" :"))
        game_player(getal, pogingSet, hvlpogingen)

    else:
        print(vraag +" wordt niet herkend, kies opniew")
        vraag()
    
def game_player(antw, pogingSet, hvlpogingen): #Game Function for against an other Player
    WStatus = False #Win Status AutoSet to lose in case something went wrong
    if pogingSet == True:
        while hvlpogingen > 0 and WStatus==False:
            print("nog", hvlpogingen ,"pogingen")
            vraag = int(input("doe een gok wat het getal is: "))
            if vraag == antw:
                print("goed geraden, dit is het juiste antwoord")
                WStatus = True
            else:
                HorL(vraag, antw)
                hvlpogingen -= 1
    else:
        vraag = None
        while vraag != antw or vraag == None:
            vraag = int(input("doe eens een gok wat het getal is: "))
            if vraag != antw:
                HorL(vraag, antw)
        else:
            print("goed geraden, dit is het juiste antwoord!")
            WStatus = True
    exit(WStatus)


def game_bot(antw, pogingSet, hvlpogingen): #Game Function for agaisnt a bot
    print(antw)
    WStatus = False
    if pogingSet == True:
        while hvlpogingen > 0 and WStatus==False:
            print("nog", hvlpogingen ,"pogingen")
            vraag = int(input("doe een gok wat het getal is: "))
            if vraag == antw:
                print("goed geraden, dit is het juiste antwoord")
                WStatus = True
            else:
                HorL(vraag, antw)
                hvlpogingen -= 1
    else:
        vraag = None
        while vraag != antw or vraag == None:
            vraag = int(input("doe eens een gok wat het getal is: "))
            if vraag != antw:
                HorL(vraag, antw)
        else:
            print("goed geraden, dit is het juiste antwoord!")
            WStatus = True
    print("het antwoord was: ", antw)
    exit(WStatus)

def HorL(vraag, antwoord): #Higher or Lower
    if vraag > antwoord:
        print("getal moet lager zijn")
    else:
        print("getal moet hoger zijn")


def exit(WOL): #Winnder or Loser
    if WOL == True:
        print("gefeliciteerd !")
    else:
        print("Jammer man")

print("welkom bij de getallen rader !")
vraag()
