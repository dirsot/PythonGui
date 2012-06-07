#!/usr/bin/python

from utils import *
	
root = Tk()

root.title("Program jakis")
meni = mojeMenu(root)

m1 = PanedWindow(root,height=35, width=40)
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane")
m1.add(left)

button1 = Button(m1, text ="Hello", command = helloCallBack)
button1.pack()

widget = SimplePlot(bg="blue", height=250, width=500)
widget.pack(side=LEFT)

widget.update() 

x=0
y=0
def rysuj():
	global x,y,widget
	x = x+1
	y = y+1
	widget.plot(x,y)
	root.after(100,rysuj)

root.after(1000,rysuj)
mainloop()
