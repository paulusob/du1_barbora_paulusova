#nejdříve je potřeba naimportovat příkazy z knihovny turtle a math
from turtle import forward, exitonclick, right, left, speed, setx, sety, setpos, circle, write, penup, pendown, home, setworldcoordinates
from math import sqrt

#spuštění hry, vysvětlení pravidel
print("Vítejte ve hře piškvorky")
print("Hráč 1 má symbol kolečka, hráč 2 má symbol křížku \nNa vyzvání zadejte nejdříve souřadnici x, poté souřadnici y vašeho tahu")


#nastavení velikosti hracího pole 
a=float(input("Zadejte počet sloupců hracího pole: ")) 
b=float(input("Zadejte počet řádků hracího pole: "))

#nastavení velikosti strany čtverce (1000 je velikost okna), která závisí na větší ze stran (a,b)
strana=1000/max(a,b)

#převedení počtu sloupců a řádků na integer
a=int(a)
b=int(b)

#nastavení velikosti okna
setworldcoordinates(-100,-100,1100,1100)

#vykreslení hracího pole
speed(0) 
for k in range(b):
    for j in range(a):
        for i in range(4): #vykreslí čtverec 
            forward(strana)
            left(90)
        forward(strana) #vykreslí řadu čtverců
    right(180)
    forward(a*strana)
    right(90)
    forward(strana)
    right(90)


#popisky hracího pole - osa x,y
penup()
setx(10+ a*strana)
sety(-5)
pendown()
write("x", move=False, align='left', font=('Arial', 8, 'normal'))
penup()
setx(0)
sety(10 + b*strana)
pendown()
write("y", move=False, align='left', font=('Arial', 8, 'normal'))

#popisky hracího pole - popisky souřadnic
for p in range(1, a+1):
    penup()
    setx(strana/2 + strana*(p-1))
    sety(-30)
    pendown()
    write(str(p), move=False, align='left', font=('Arial', 8, 'normal'))

for q in range(1, b+1):
    penup()
    setx(-30)
    sety(strana/2 + strana*(q-1))
    pendown()
    write(str(q), move=False, align='left', font=('Arial', 8, 'normal'))
penup()
home()
pendown()


#začátek hry 
#počet tahů závisí na velikosti hracího pole, přičemž při lichém počtu políček má hráč 1 tah navíc 

m=int((a*b)/2) #výpočet počtu tahů 

for l in range (m): # následující kroky se opakují m* podle počtu políček 
    print("Je na tahu hráč 1")
    v=float(input("Zadejte x souřadnici v intervalu hracího pole: ")) #hráč zadá souřadnice, na které se vykreslí znak
    while v>a or v<1: #podmínka, že x (resp. y) musí být v dříve nastaveném intervalu podle nákresu hracího pole
        # - pokud není splněna, uživatel je vyzván k zadání jiného čísla v zadaném intervalu
        print("x musí být v intervalu hracího pole")
        v=float(input("Zadejte znovu x souřadnici v intervalu hracího pole: "))

    x=(v-1)*strana #převedení relativních souřadnic hracího pole na absolutní souřadnice
 
    s=float(input("Zadejte y souřadnici hracího pole: "))
    while s>b or s<1:
        print("y musí být v intervalu hracího pole")
        s=float(input("Zadejte znovu y souřadnici v intervalu hracího pole: "))
    
    y=(s-1)*strana #převedení relativních souřadnic hracího pole na absolutní souřadnice

    #nastavení souřadnic, na kterých se bude kreslit symbol
    setx(x) 
    sety(y)  

    #vykreslení kruhu
    forward (strana/2) 
    circle(strana/2) 
    left(180) 
    forward(strana/2)
    left(180)
    #konec tahu prvního hráče
    

    # je na řadě hráč 2, proces je stejný jako u hráče 1, s výjimkou vykreslení křížku místo kolečka
    print("Je na tahu hráč 2")
    v=float(input("Zadejte x souřadnici v intervalu hracího pole: "))
    while v>a or v<1:
        print("x musí být v intervalu hracího pole")
        v=float(input("Zadejte znovu x souřadnici v intervalu hracího pole: "))
    
    x=(v-1)*strana

    s=float(input("Zadejte y souřadnici hracího pole: "))
    while s>b or s<1:
        print("y musí být v intervalu hracího pole")
        s=float(input("Zadejte znovu y souřadnici v intervalu hracího pole: "))
    
    y=(s-1)*strana

    setx(x)
    sety(y)

    #vykreslení křížku
    left(45)
    forward (sqrt(2*(strana**2)))
    left(135)
    forward(strana)
    left(135)
    forward(sqrt(2*(strana**2)))
    right(135)
    forward(strana)
    left(180)

n=int((a*b)%2) #případný poslední tah, pokud je lichý počet polí
for _ in range (n): 
    print("Je na tahu hráč 1")
    v=float(input("Zadejte x souřadnici v intervalu hracího pole: "))
    while v>a or v<1:
        print("x musí být v intervalu hracího pole")
        v=float(input("Zadejte znovu x souřadnici v intervalu hracího pole: "))

    x=(v-1)*strana

    s=float(input("Zadejte y souřadnici  intervalu hracího pole: "))
    while s>b or s<1:
        print("y musí být v intervalu hracího pole")
        s=float(input("Zadejte znovu y souřadnici v intervalu hracího pole: "))

    y=(s-1)*strana

    setx(x)
    sety(y)

    forward (strana/2) 
    circle(strana/2) 
    left(180) 
    forward(strana/2)
    left(180)
print("Konec hry")
exitonclick()