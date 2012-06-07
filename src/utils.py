from Tkinter import *
from menu import mojeMenu
import tkMessageBox

class SimplePlot(Canvas):
	
	def plot(self, x, y):
		self.create_line((x, y, x+1, y), fill="black")

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")
