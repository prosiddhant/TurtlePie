import turtle
import math
t =  turtle.Turtle()

def turtlepies(t,length,n):
	x = 360 - (360/n)
	y = (length/2)/(math.sin(math.radians(180/n)))
	for i in range(n):
		t.fd(length)
		t.lt(90 + (180/n))
		t.fd(y)
		t.lt(x)
		t.bk(y)
		t.lt(90 + (180/n))
		t.pu()
		t.bk(length)	
		t.pd()
		t.lt(180 + (360/n))
t.hideturtle()			
turtlepies(t,120,12)
turtle.mainloop()