import random

a= " "
clovekvysledek = 0
pocitacvysledek = 0

def Clovek():
    clovek = input("Zvolte si kámen, nůžky nebo papír. Pro kámen napište k, pro nůžky napište n, pro papír napište p:   ")
    if clovek not in ["k", "n", "p"]:
        clovek = 0
    return clovek

def Pocitac():
    pocitac = random.choice(["k", "n", "p"])
    return pocitac

while a != "konec":
    clovek = Clovek()
    pocitac = Pocitac()

    if clovek == 0:
        print ("Napsal jste neplatný znak, zkuste to znovu")
        a = input("Pokud nechcete pokračovat, napište: konec   ")

    else:
        if clovek == pocitac:
            print ("Zvolil jste   " + clovek)
            print ("Počítač zvolil   " + pocitac)
            print ("Výsledek: REMÍZA")
            print ("Průběžné pořadí - člověk: " + str(clovekvysledek) + " počítač: " + str(pocitacvysledek))
            a = input("Pokud nechcete pokračovat, napište: konec   ")

        elif clovek == "k" and pocitac == "n" or clovek == "n" and pocitac == "p" or clovek == "p" and pocitac == "k":
            clovekvysledek+=1
            print ("Zvolil jste   " + clovek)
            print ("Počítač zvolil   " + pocitac)
            print ("Výsledek: VYHRÁL JSI")
            print ("Průběžné pořadí - člověk: " + str(clovekvysledek) + " počítač: " + str(pocitacvysledek))
            a = input("Pokud nechcete pokračovat, napište: konec   ")
            
        else:
            pocitacvysledek+=1
            print ("Zvolil jste   " + clovek)
            print ("Počítač zvolil   " + pocitac)
            print ("Výsledek: VYHRÁL POČÍTAČ")
            print ("Průběžné pořadí - člověk: " + str(clovekvysledek) + " počítač: " + str(pocitacvysledek))
            a = input("Pokud nechcete pokračovat, napište: konec   ")
