from turtle import forward, exitonclick, right, left, speed, setx, sety, setpos, circle, write, penup, pendown, home
print("Vítejte ve hře piškvorky")
print("Hráč 1 má symbol kolečka, hráč 2 má symbol křížku, Na vyzvání zadejte nejdříve souřadnici x, posléze souřadnici y vašeho tahu")


#vykresleni ctvercove site 
a=3
b=3
strana=100
speed(0)
for k in range(b):
    for j in range(a):
        for i in range(4):
            forward(strana)
            left(90)
        forward(strana)
    right(180)
    forward(a*strana)
    right(90)
    forward(strana)
    right(90)
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
for l in range (4):
    print("Je na tahu hráč 1")
    x=float(input("Zadejte x souřadnici (1-3): "))
    if x==1:
        x=0
    elif x==2:
        x=100
    else:
        x=200
    y=float(input("Zadejte y souřadnici: "))
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
    print("Je na tahu hráč 2")
    x=float(input("Zadejte x souřadnici: "))
    if x==1:
        x=0
    elif x==2:
        x=100
    else:
        x=200
    y=float(input("Zadejte y souřadnici: "))
    if y==1:
        y=0
    elif y==2:
        y=100
    else:
        y=200
    setx(x)
    sety(y)
    left(45)
    forward (141.42)
    left(135)
    forward(100)
    left(135)
    forward(141.42)
    right(135)
    forward(100)
    left(180)
print("Je na tahu hráč 1")
x=float(input("Zadejte x souřadnici: "))
if x==1:
        x=0
    elif x==2:
        x=100
    else:
        x=200
y=float(input("Zadejte y souřadnici: "))
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