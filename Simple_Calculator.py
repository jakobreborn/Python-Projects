from tkinter import *

#import math

glowneOkno=Tk()
opcja=IntVar()

def Kalk():
    if opcja.get()==1:
        c=int(pole1.get())+ int(pole2.get())
    if opcja.get()==2:
        c=int(pole1.get())- int(pole2.get())
    if opcja.get()==3:
        c=int(pole1.get())* int(pole2.get())
    if opcja.get()==4:
        c=round(int(pole1.get())/int(pole2.get()),2)
    if opcja.get()==5:
        c="               0                "

    pole3=Label(glowneOkno,text=str(c))
    pole3.grid(row=5, column=1)


glowneOkno.title("Kalkulator")


###### Przyciski do działań: +, -, *, /

plus=Radiobutton(glowneOkno, text ="+", variable=opcja , value=1, command=Kalk)
plus.grid()

minus=Radiobutton(glowneOkno, text ="-", variable=opcja , value=2, command=Kalk)
minus.grid()

razy=Radiobutton(glowneOkno, text ="*", variable=opcja , value=3, command=Kalk)
razy.grid()

przez=Radiobutton(glowneOkno, text ="/", variable=opcja , value=4, command=Kalk)
przez.grid()

zerowanie=Radiobutton(glowneOkno, text="C", bg="red", variable=opcja, value=5, command=Kalk)
zerowanie.grid(row=0, column=5)

###### Podstawa kalkulatora - opis pól i pola

opis1=Label(glowneOkno ,text="a")
opis1.grid (row=0, column=1)
opis2=Label(glowneOkno ,text="b")
opis2.grid (row=2, column=1)
opis3=Label(glowneOkno ,text="Wynik")
opis3.grid (row=4, column=1)

pole1=Entry(glowneOkno)
pole1.grid(row=1, column=1)
pole2=Entry(glowneOkno)
pole2.grid(row=3, column=1)

##### Przycsik do obliczania

przycisk1=Button(glowneOkno, text ="Oblicz", command=Kalk)
przycisk1.grid(row=2, column=4)


###### Podpis pola z wynikiem

pole3=Label(glowneOkno,text="0")
pole3.grid(row=5, column=1)


glowneOkno.mainloop ()
