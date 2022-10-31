#nejdříve je potřeba naimportovat příkazy z knihovny turtle
from turtle import forward, exitonclick, right, left, speed, setx, sety, setpos, circle, write, penup, pendown, home
#spuštění hry, vysvětlení pravidel
print("Vítejte ve hře piškvorky")
print("Hráč 1 má symbol kolečka, hráč 2 má symbol křížku \nNa vyzvání zadejte nejdříve souřadnici x, poté souřadnici y vašeho tahu")
#vykreslení čtvercové sítě, zatím o velikosti 3*3 
a=3
b=3
strana=100
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
#popisky hracího pole - osa x,y a interval (1,3)
penup()
setx(310)
sety(-5)
pendown()
write ("x",move=False, align='left',font=('Arial',8,'normal'))
penup()
setx(0)
sety(310)
pendown()
write ("y",move=False, align='left',font=('Arial',8,'normal'))
penup()
setx(45)
sety(-20)
pendown()
write ("1",move=False, align='left',font=('Arial',8,'normal'))
penup()
setx(145)
sety(-20)
pendown()
write ("2",move=False, align='left',font=('Arial',8,'normal'))
penup()
setx(245)
sety(-20)
pendown()
write ("3",move=False, align='left',font=('Arial',8,'normal'))
penup()
setx(-20)
sety(45)
pendown()
write ("1",move=False, align='left',font=('Arial',8,'normal'))
penup()
setx(-20)
sety(145)
pendown()
write ("2",move=False, align='left',font=('Arial',8,'normal'))
penup()
setx(-20)
sety(245)
pendown()
write ("3",move=False, align='left',font=('Arial',8,'normal'))
penup()
home()
pendown()
#začátek hry 
#v hracím poli je dohromady 9 políček - hráč 1 má tedy 5 tahů, hráč 2 má 4 tahy, poslední tah prvního hráče je uveden zvlášť
for l in range (4): #4 tahy jsou pro oba hráče společné - 4* se tedy opakují následující kroky 
    print("Je na tahu hráč 1")
    x=float(input("Zadejte x souřadnici v intervalu (1-3): ")) #hráč zadá souřadnice, na které se vykreslí znak
    while x>3 or x<1: #podmínka, že x (resp. y) musí být v inervalu (1,3) podle nákresu hracího pole
        # - pokud není splněna, uživatel je vyzván k zadání jiného čísla v intervalu (1,3)
        print("x musí být v intervalu (1,3)")
        x=float(input("Zadejte znovu x souřadnici v intervalu (1-3): "))
    if x==1: #převedení relativních souřadnic hracího pole na absolutní souřadnice
        x=0
    elif x==2:
        x=100
    else:
        x=200
    y=float(input("Zadejte y souřadnici (1-3): "))
    while y>3 or y<1:
        print("y musí být v intervalu (1,3)")
        y=float(input("Zadejte znovu y souřadnici v intervalu (1-3): "))
    if y==1:
        y=0
    elif y==2:
        y=100
    else:
        y=200
    #nastavení souřadnic, na kterých se bude kreslit symbol
    setx(x) 
    sety(y)  
    #vykreslení kruhu
    forward (50) 
    circle(50) 
    left(180) 
    forward(50)
    left(180)
    #konec tahu prvního hráče, je na řadě hráč 2, proces je stejný jako u hráče 1, s výjimkou vykreslení křížku místo kolečka
    print("Je na tahu hráč 2")
    x=float(input("Zadejte x souřadnici (1-3): "))
    while x>3 or x<1:
        print("x musí být v intervalu (1,3)")
        x=float(input("Zadejte znovu x souřadnici v intervalu (1-3): "))
    if x==1:
        x=0
    elif x==2:
        x=100
    else:
        x=200
    y=float(input("Zadejte y souřadnici (1-3): "))
    while y>3 or y<1:
        print("y musí být v intervalu (1,3)")
        y=float(input("Zadejte znovu y souřadnici v intervalu (1-3): "))
    if y==1:
        y=0
    elif y==2:
        y=100
    else:
        y=200
    setx(x)
    sety(y)
    #vykreslení křížku
    left(45)
    forward (141.42)
    left(135)
    forward(100)
    left(135)
    forward(141.42)
    right(135)
    forward(100)
    left(180)
#poslední tah prvního hráče, taktéž stejný proces 
print("Je na tahu hráč 1")
x=float(input("Zadejte x souřadnici (1-3): "))
while x>3 or x<1:
    print("x musí být v intervalu (1,3)")
    x=float(input("Zadejte znovu x souřadnici v intervalu (1-3): "))
if x==1:
    x=0
elif x==2:
    x=100
else:
    x=200
y=float(input("Zadejte y souřadnici (1-3): "))
while y>3 or y<1:
    print("y musí být v intervalu (1,3)")
    y=float(input("Zadejte znovu y souřadnici v intervalu (1-3): "))
if y==1:
    y=0
elif y==2:
    y=100
else:
    y=200
setx(x)
sety(y)
forward (50)
circle(50)
left(180)
forward(50)
left(180)
print("Konec hry")
exitonclick()