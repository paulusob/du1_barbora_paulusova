from turtle import forward, exitonclick, right, left, speed, setx, sety, setpos, circle
print("Vítejte ve hře piškvorky")
print("Hráč 1 má symbol kolečka, hráč 2 má symbol křížku, Na vyzvání zadejte nejdříve souřadnici x, posléze souřadnici y vašeho tahu")


#vykresleni ctvercove site 
a=3
b=3
strana=100
speed(9)
for k in range(b):
	# Nakreslí řádek
	for j in range(a):
		# Nakreslí čtverec
		for i in range(4):
			forward(strana)
			left(90)
		forward(strana)
	right(180)
	forward(a*strana)
	right(90)
	forward(strana)
	right(90)
print("Je na tahu hráč 1")
x=float(input("Zadejte x souřadnici: "))
y=float(input("Zadejte y souřadnici: "))
setx(x)
sety(y)
forward (50)
circle(50)
left(180)
forward(50)
left(180)
print("Je na tahu hráč 2")
x=float(input("Zadejte x souřadnici: "))
y=float(input("Zadejte y souřadnici: "))
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
exitonclick()