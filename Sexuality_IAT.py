import random, time, os

wszystko=("Uwielbiać", "Zachwycać się", "Fantastyczny", "Piękny", "Triumfalny", "Chwalebny", "Miłość", "Ból", "Okropny", "Chory", "Smutek", "Zgniły", "Brzydki", "Obrzydzenie", "Porażka", "Geje", "Homo", "Lesbijki", " Nieheteronormatywny", "Hetero", "Orientacja heteroseksualna", "Heteryk")
dobrezle=("Uwielbiać", "Zachwycać się", "Fantastyczny", "Piękny", "Triumfalny", "Chwalebny", "Miłość", "Ból", "Okropny", "Chory", "Smutek", "Zgniły", "Brzydki", "Obrzydzenie", "Porażka")
homohetero=("Geje", "Homo", "Lesbijki", "Heteryk", "Nieheteronormatywny", "Hetero", "Orientacja heteroseksualna")

dobre=("Uwielbiać", "Zachwycać się", "Fantastyczny", "Piękny", "Triumfalny", "Chwalebny", "Miłość")
zle=("Ból", "Okropny", "Chory", "Smutek", "Zgniły", "Brzydki", "Obrzydzenie", "Porażka")
homoseksualni=("Geje", "Homo", "Lesbijki", "Nieheteronormatywny")
heteroseksualni=("Hetero", "Orientacja heteroseksualna", "Heteryk")

czasy_homo=0
czasy_hetero=0
czasy_dobre=0
czasy_zle=0
czasy_homo_dobre=0
czasy_hetero_dobre=0
czasy_homo_zle=0
czasy_hetero_zle=0

print("Część 1/7 \n")

b_start=input("Wciśnij (E) żęby zaznaczyć HOMO, wciśnij(I) żeby zaznaczyć HETERO\n"\
      "                                 ŻEBY ROZPOCZĄĆ WCIŚNIJ (B)                  ")
while b_start!="b":
    b_start=input("Wciśnij (E) żęby zaznaczyć HOMO, wciśnij(I) żeby zaznaczyć HOMO\n"\
      "                                 ŻEBY ROZPOCZĄĆ WCIŚNIJ (B)                     ")

for i in range(10):
    os.system("cls")
    los=random.choice(homohetero)
    print("Homo                                                  Hetero\n"\
          "  E                                                          I\n")
    print("\n\n\n\n\n\n", "                      ", los)
    start=time.time()
    odp=input()
    koniec=time.time()
    rt=koniec-start
    if los in homoseksualni and odp=="e":
        czasy_homo+=rt
    elif los in homoseksualni and odp=="i":
       
        while odp!="e":
            print("                          ŹLE")
            odp=input()
            
            
        else:
            czasy_homo+=rt
    elif los in heteroseksualni and odp=="i":
        czasy_hetero+=rt
    elif los in heteroseksualni and odp=="e":

        while odp!="i":
            print("                          ŹLE")
            odp=input()
            
        else:
            czasy_hetero+=rt
    else:
        print("                              ŹLE")

print("Część 2/7 \n")

b_start=input("Wciśnij (E) żęby zaznaczyć DOBRE, wciśnij(I) żeby zaznaczyć ZLE\n"\
      "                                 ŻEBY ROZPOCZĄĆ WCIŚNIJ (B)                  ")
while b_start!="b":
    b_start=input("Wciśnij (E) żęby zaznaczyć DOBRE, wciśnij(I) żeby zaznaczyć ZLE\n"\
      "                                 ŻEBY ROZPOCZĄĆ WCIŚNIJ (B)                     ")

for i in range(10):
    os.system("cls")
    los=random.choice(dobrezle)
    print("Dobre                                                  Zle\n"\
          "  E                                                          I\n")
    print("\n\n\n\n\n\n", "                      ", los)
    start=time.time()
    odp=input()
    koniec=time.time()
    rt=koniec-start
    if los in dobre and odp=="e":
        czasy_dobre+=rt
    elif los in dobre and odp=="i":
       
        while odp!="e":
            print("                          ŹLE")
            odp=input()
            
            
        else:
            czasy_dobre+=rt
    elif los in zle and odp=="i":
        czasy_zle+=rt
    elif los in zle and odp=="e":

        while odp!="i":
            print("                          ŹLE")
            odp=input()
            
        else:
            czasy_zle+=rt
    else:
        print("                              ŹLE")

print("Część 3/7 \n")

b_start=input("Wciśnij (E) żęby zaznaczyć DOBRE/HETERO, wciśnij(I) żeby zaznaczyć ZLE/HOMO\n"\
      "                                 ŻEBY ROZPOCZĄĆ WCIŚNIJ (B)                  ")
while b_start!="b":
    b_start=input("Wciśnij (E) żęby zaznaczyć DOBRE/HETERO, wciśnij(I) żeby zaznaczyć ZLE/HOMO\n"\
      "                                 ŻEBY ROZPOCZĄĆ WCIŚNIJ (B)                     ")

for i in range(10):
    os.system("cls")
    los=random.choice(wszystko)
    print("   DOBRE                                                 ZLE\n"\
          "   lub                                                   lub\n"\
          "   HETERO                                                HOMO\n"\
          "   (E)                                                   (I)\n")
    print("\n\n\n\n\n\n", "                      ", los)
    start=time.time()
    odp=input()
    koniec=time.time()
    rt=koniec-start
    if los in dobre or los in heteroseksualni and odp=="e":
        czasy_hetero_dobre+=rt
    elif los in dobre or los in heteroseksualni and odp=="i":
       
        while odp!="e":
            print("                          ŹLE")
            odp=input()
            
            
        else:
            czasy_hetero_dobre+=rt
    elif los in zle or los in homoseksualni and odp=="i":
        czasy_homo_zle+=rt
    elif los in zle or los in homoseksualni and odp=="e":

        while odp!="i":
            print("                          ŹLE")
            odp=input()
            
        else:
            czasy_homo_zle+=rt
    else:
        print("                              ŹLE")



print("Część \n")

b_start=input("Wciśnij (E) żęby zaznaczyć DOBRE/HOMO, wciśnij(I) żeby zaznaczyć ZLE/HETERO\n"\
      "                                 ŻEBY ROZPOCZĄĆ WCIŚNIJ (B)                  ")
while b_start!="b":
    b_start=input("Wciśnij (E) żęby zaznaczyć DOBRE/HOMO, wciśnij(I) żeby zaznaczyć ZLE/HETERO\n"\
      "                                 ŻEBY ROZPOCZĄĆ WCIŚNIJ (B)                     ")

for i in range(10):
    os.system("cls")
    los=random.choice(wszystko)
    print("   DOBRE                                                 ZLE\n"\
          "   lub                                                   lub\n"\
          "   HOMO                                                  HETERO\n"\
          "   (E)                                                   (I)\n")
    print("\n\n\n\n\n\n", "                      ", los)
    start=time.time()
    odp=input()
    koniec=time.time()
    rt=koniec-start
    if los in dobre or los in homoseksualni and odp=="e":
        czasy_homo_dobre+=rt
    elif los in dobre or los in homoseksualni and odp=="i":
       
        while odp!="e":
            print("                          ŹLE")
            odp=input()
            
            
        else:
            czasy_homo_dobre+=rt
    elif los in zle or los in heteroseksualni and odp=="i":
        czasy_hetero_zle+=rt
    elif los in zle or los in heteroseksualni and odp=="e":

        while odp!="i":
            print("                          ŹLE")
            odp=input()
            
        else:
            czasy_hetero_zle+=rt
    else:
        print("                              ŹLE")



print("Część 5/7 \n")

b_start=input("Wciśnij (E) żęby zaznaczyć HETERO, wciśnij(I) żeby zaznaczyć HOMO\n"\
      "                                 ŻEBY ROZPOCZĄĆ WCIŚNIJ (B)                  ")
while b_start!="b":
    b_start=input("Wciśnij (E) żęby zaznaczyć HETERO, wciśnij(I) żeby zaznaczyć HOMO\n"\
      "                                 ŻEBY ROZPOCZĄĆ WCIŚNIJ (B)                     ")
    
    

for i in range(10):
    os.system("cls")
    los=random.choice(homohetero)
    print("HETERO                                                  HOMO\n"\
          "  (E)                                                          (I)\n")
    print("\n\n\n\n\n\n", "                      ", los)
    start=time.time()
    odp=input()
    koniec=time.time()
    rt=koniec-start
    if los in heteroseksualni and odp=="e":
        czasy_homo+=rt
    elif los in heteroseksualni and odp=="i":
       
        while odp!="e":
            print("                          ŹLE")
            odp=input()
            
            
        else:
            czasy_hetero+=rt
    elif los in homoseksualni and odp=="i":
        czasy_hetero+=rt
    elif los in homoseksualni and odp=="e":

        while odp!="i":
            print("                          ŹLE")
            odp=input()
            
        else:
            czasy_homo+=rt
    else:
        print("                              ŹLE")

print("Część 6/7 \n")


b_start=input("Wciśnij (E) żęby zaznaczyć DOBRE/HOMO, wciśnij(I) żeby zaznaczyć ZLE/HETERO\n"\
      "                                 ŻEBY ROZPOCZĄĆ WCIŚNIJ (B)                  ")
while b_start!="b":
    b_start=input("Wciśnij (E) żęby zaznaczyć DOBRE/HOMO, wciśnij(I) żeby zaznaczyć ZLE/HETERO\n"\
      "                                 ŻEBY ROZPOCZĄĆ WCIŚNIJ (B)                     ")
    
for i in range(10):
    os.system("cls")
    los=random.choice(wszystko)
    print("   DOBRE                                                 ZLE\n"\
          "   lub                                                   lub\n"\
          "   HOMO                                                  HETERO\n"\
          "   (E)                                                   (I)\n")
    print("\n\n\n\n\n\n", "                      ", los)
    start=time.time()
    odp=input()
    koniec=time.time()
    rt=koniec-start
    if los in dobre or los in homoseksualni and odp=="e":
        czasy_homo_dobre+=rt
    elif los in dobre or los in homoseksualni and odp=="i":
       
        while odp!="e":
            print("                          ŹLE")
            odp=input()
            
            
        else:
            czasy_homo_dobre+=rt
    elif los in zle or los in heteroseksualni and odp=="i":
        czasy_hetero_zle+=rt
    elif los in zle or los in heteroseksualni and odp=="e":

        while odp!="i":
            print("                          ŹLE")
            odp=input()
            
        else:
            czasy_hetero_zle+=rt
    else:
        print("                              ŹLE")



print("Część 7/7 \n")

b_start=input("Wciśnij (E) żęby zaznaczyć DOBRE/HOMO, wciśnij(I) żeby zaznaczyć ZLE/HETERO\n"\
      "                                 ŻEBY ROZPOCZĄĆ WCIŚNIJ (B)                  ")
while b_start!="b":
    b_start=input("Wciśnij (E) żęby zaznaczyć DOBRE/HOMO, wciśnij(I) żeby zaznaczyć ZLE/HETERO\n"\
      "                                 ŻEBY ROZPOCZĄĆ WCIŚNIJ (B)                     ")


for i in range(10):
    os.system("cls")
    los=random.choice(wszystko)
    print("   DOBRE                                                 ZLE\n"\
          "   lub                                                   lub\n"\
          "   HOMO                                                  HETERO\n"\
          "   (E)                                                   (I)\n")
    print("\n\n\n\n\n\n", "                      ", los)
    start=time.time()
    odp=input()
    koniec=time.time()
    rt=koniec-start
    if los in dobre or los in homoseksualni and odp=="e":
        czasy_homo_dobre+=rt
    elif los in dobre or los in homoseksualni and odp=="i":
       
        while odp!="e":
            print("                          ŹLE")
            odp=input()
            
            
        else:
            czasy_homo_dobre+=rt
    elif los in zle or los in heteroseksualni and odp=="i":
        czasy_hetero_zle+=rt
    elif los in zle or los in heteroseksualni and odp=="e":

        while odp!="i":
            print("                          ŹLE")
            odp=input()
            
        else:
            czasy_hetero_zle+=rt
    else:
        print("                              ŹLE")

print("PODSUMOWANIE\n")

if czasy_hetero_zle<czasy_homo_dobre:
    print("Posiadasz ukryte uprzedzenia wobec osób heteroseksualnych!")
elif czasy_homo_zle<czasy_hetero_dobre:
    print("Posiadasz ukryte uprzedzenia wobec osób homoseksualnych")
elif czasy_homo_dobre>czasy_hetero_zle:
    print("Nie posiadasz ukrytych uprzedzeń wobec osób heteroseksualnych")
elif czasy_hetero_dobre>czasy_homo_zle:
    print("Nie posiadasz ukrytych uprzedzeń wobec osób homoseksualnych")



