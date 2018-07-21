import turtle
import math
t =  turtle.Turtle()
def turtlepies(t,length,n):	
	y = (length/2)/math.sin(math.radians(180/n))
	for i in range(n):
		t.fd(length)
		t.lt(90 + (180/n))
		t.fd(y)
		t.lt(180)
		t.pu()
		t.fd(y)
		t.lt(90 + (180/n))
		t.pd()		
turtlepies(t,100,6)
turtle.mainloop()