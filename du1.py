from turtle import forward, exitonclick, right, left, speed

#vykresleni ctvercove site 
a=3
b=3
strana=100

speed(0)
for y in range(b):
	# Nakreslí řádek
	for x in range(a):
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
exitonclick()

