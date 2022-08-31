import random, time, winsound




print("ZADANIE 4: OKRUTNY BUDZIK \n")

opcja=int(input("WYBIERZ OPCJĘ BUDZENIA: 1) LIGHT 2) PRO \n"))
dobre_odpowiedzi=0








if opcja==1:
    print("OPCJA LIGHT: BUDZENIE PRZEZ DODAWANIE =) \n")
    
    
    
    while dobre_odpowiedzi < 5:
        winsound.PlaySound("SystemAsterisk", winsound.SND_LOOP + winsound.SND_ASYNC)
        while True:
            
            liczba1=random.randint(10,99)
            liczba2=random.randint(10,99)

            start=time.time()
        
            print(liczba1, "+", liczba2)
            odp=int(input("podaj wynik [masz na to TYLKO 10 SEKUND =)]\n"))
        

            koniec=time.time()
        
            rt=koniec-start

        

        
        
            if odp==liczba1+liczba2 and rt<10:
                print("DOBRZE!")
            
                dobre_odpowiedzi+=1
                break

            
            elif rt<10:
                print("MINĘŁO JUŻ 10 SEKUND!")
            else:
                print("ŹLE!")
        winsound.PlaySound(None, winsound.SND_LOOP + winsound.SND_ASYNC)

if opcja==2:
    print("OPCJA PRO: BUDZENIE PRZEZ MNOŻENIE =) \n")
    
    
    
    while dobre_odpowiedzi < 5:
        winsound.PlaySound("SystemAsterisk", winsound.SND_LOOP + winsound.SND_ASYNC)
        while True:
            
            liczba1=random.randint(1,9)
            liczba2=random.randint(1,9)

            start=time.time()
        
            print(liczba1, "*", liczba2)
            odp=int(input("podaj wynik [masz na to TYLKO 10 SEKUND =)]\n"))
        

            koniec=time.time()
        
            rt=koniec-start

        

        
        
            if odp==liczba1*liczba2 and rt<10:
                print("DOBRZE!")
            
                dobre_odpowiedzi+=1
                break

            
            elif rt<10:
                print("MINĘŁO JUŻ 10 SEKUND")
            else:
                print("ŹLE!")
        winsound.PlaySound(None, winsound.SND_LOOP + winsound.SND_ASYNC)
        
            


        
        
    


