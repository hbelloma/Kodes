#run online with https://create.withcode.uk/
#or use https://repl.it/languages/tkinter
# this program makes rownian movement

from tkinter import *
from random import*
#parametro del sistema 
x=100
y=100
lx=600
ly=600
x=300
y=300
tampaso=5.0
#la ventana
w=Tk()
w.title("browniano")
c=Canvas(w,width=lx,height=ly,bg="green")
c.pack()
pelota1=c.create_oval(x-10,y-10,x+10,y+10,fill="blue")
pelota2=c.create_oval(x-10,y-10,x+10,y+10,fill="blue")
pelota3=c.create_oval(x-10,y-10,x+10,y+10,fill="blue")
pelota4=c.create_oval(x-10,y-10,x+10,y+10,fill="blue")
def mover():
	global x,y
	dx1=-tampaso+2*tampaso*random()
	dy1=-tampaso+2*tampaso*random()
	c.move(pelota1,dx1,dy1)
	dx2=-tampaso+2*tampaso*random()
	dy2=-tampaso+2*tampaso*random()
	c.move(pelota2,dx2,dy2)
	dx3=-tampaso+2*tampaso*random()
	dy3=-tampaso+2*tampaso*random()
	c.move(pelota3,dx3,dy3)
	dx4=-tampaso+2*tampaso*random()
	dy4=-tampaso+2*tampaso*random()
	c.move(pelota4,dx4,dy4)
	w.after(100,mover)
mover()
w.mainloop()