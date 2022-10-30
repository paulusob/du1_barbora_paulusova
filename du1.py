from turtle import forward, exitonclick, right, left, speed, setx, sety, setpos, circle
print("Vítejte ve hře piškvorky")
print("Hráč 1 má symbol křížku, hráč 2 má symbol kolečka, Na vyzvání zadejte nejdříve souřadnici x, posléze souřadnici y vašeho tahu")
print("Je na tahu hráč 1")

x=float(input("Zadejte x souřadnici: "))
y=float(input("Zadejte y souřadnici: "))
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
setx(x)
sety(y)
forward (50)
circle(50)
left(180)
forward(50)
left(180)
exitonclick()