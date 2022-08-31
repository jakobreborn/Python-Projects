import time, random
### dwa poniżej przed standardowym importowaniem trzeba najpierw zainstalować przez "pip install" w cmd
from colorama import init
from termcolor import colored

init()

    
zgodne=0 # licznik do wystąpień serii zgodnej
poprawne_zgodne=0
poprawne_niezgodne=0
niezgodne=0 # licznik do wystąpień serii niezgodnej
suma=0 # licznik do poprawnych odpowiedzi


slowa=("green", "yellow", "red", "blue")
czcionki=("green", "yellow", "red", "blue")

srednia_global=0
srednia_zgodne=0
srednia_niezgodne=0


print("Witaj w badaniu efektu Stroopa! Przed Tobą 20 pytań, skoncentruj się dobrze. Gotów? Start!")

time.sleep(2)

for i in range(20): ##20 powinno być
    slowo=random.choice(slowa)
    czcionka=random.choice(czcionki)
    start=time.time()
    print(colored(slowo, czcionka))
    odp=int(input("Jakim kolorem jest napisany wyraz? \n 1 - zielonym \n 2 - żółtym \n 3 - czerwonym \n 4 - niebieskim? \n"))
    koniec=time.time()
    czasReakcji=koniec-start
    if slowo==czcionka and zgodne>=niezgodne and zgodne>=10 or niezgodne>=zgodne and niezgodne>=10:
        print("To było pytanie z serii zgodne!")
        zgodne+=1
        
        if (czcionka==czcionki[0] and odp==1) or (czcionka==czcionki[1] and odp==2) or (czcionka==czcionki[2] and odp==3) or (czcionka==czcionki[3] and odp==4):
            suma+=1
            srednia_global+=czasReakcji
            srednia_zgodne+=czasReakcji
            poprawne_zgodne+=1
            print("Dobrze!")
        else:
            print("Źle")
    else:
        print("To było pytanie z serii niezgodne!")
        niezgodne+=1

        if (czcionka==czcionki[0] and odp==1) or (czcionka==czcionki[1] and odp==2) or (czcionka==czcionki[2] and odp==3) or (czcionka==czcionki[3] and odp==4):
            suma+=1
            srednia_global+=czasReakcji
            srednia_niezgodne+=czasReakcji
            poprawne_niezgodne+=1

            print("Dobrze!")
        else:
            print("Źle")


            

print("Twój czas reakcji to", czasReakcji)

print(srednia_global)
print("\n@@@@@@@@@@@@@@@@@@   PODSUMOWANIE   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")

print("Łącznie pojawiło się", zgodne, "pytań z serii zgodne. Udzieliłeś",(poprawne_zgodne/zgodne)*100,"% poprawnych odpowiedzi.")
print("Łącznie pojawiło się", niezgodne, "pytań z serii niezgodne. Udzieliłeś",(poprawne_niezgodne/niezgodne)*100, "% poprawnych odpowiedzi.")
print("Łącznie udzieliłeś",(suma/20)*100 ,"% poprawnych odpowiedzi.")
print("Łączny średni czas to ",round(srednia_global/20, 2),"s. średni czas dla serii zgodne to",round(srednia_zgodne/zgodne, 2),"s. a dla serii niezgodne to", round(srednia_niezgodne/niezgodne, 2), "s.")

odp=int(input("KLIKINIJ (ENTER) ABY WYŁĄCZYĆ SKRYPT!!!"))
