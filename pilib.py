
                                 # AUTOMATIC LIBRARY ISSUE GRAPHICAL USER INTERFACE BASED ON TKINTER AND PYSERIAL

from Tkinter import *
import tkMessageBox
import tkFont
import threading
import time 
from serial import *
import random
from PIL import Image, ImageTk
from itertools import count

serialPort = '/dev/ttyACM0'
baudrate = 9600
ser = Serial(serialPort , baudrate, timeout=0, writeTimeout=0) #non blocking             # SERIAL PORT DECLARATION
#ser = serial.Serial('/dev/ttyACMO',9600)

class nitc:
	def __init__ (self,master):
		frame = Frame(master)
		frame.pack()

		self.printButton = Button(frame,text = "WELCOME TO NITC CENTRAL LIBRARY", font = myFont1 , bg ="YELLOW",fg ="RED")
		self.printButton.pack(side = TOP)

		self.printButton = Button(frame,text = "EXIT",font = myFont ,command = frame.quit,height =2 , width = 6)
		self.printButton.pack(side = BOTTOM)

		self.printmButton = Button(frame,text = "ABOUT",font = myFont ,command = self.printm,height =2 , width = 6)
		self.printmButton.pack(side = BOTTOM)

		self.press1Button = Button(frame,text = "1",font = myFont ,command = self.press1,height =2 , width = 6)
		self.press1Button.pack(side = LEFT)

		self.press2Button = Button(frame,text = "2",font = myFont ,command = self.press2,height =2 , width = 6)
		self.press2Button.pack(side = LEFT)

		self.press3Button = Button(frame,text = "3",font = myFont ,command = self.press3,height =2 , width = 6)
		self.press3Button.pack(side = LEFT)

		self.press4Button = Button(frame,text = "4",font = myFont ,command = self.press4,height =2 , width = 6)                  # FUNCTION DECLARATION
		self.press4Button.pack(side = LEFT)

		self.press5Button = Button(frame,text = "5",font = myFont ,command = self.press5,height =2 , width = 6)
		self.press5Button.pack(side = LEFT)

		self.press6Button = Button(frame,text = "6",font = myFont ,command = self.press6,height =2 , width = 6)
		self.press6Button.pack(side = LEFT)

		self.press7Button = Button(frame,text = "7",font = myFont ,command = self.press7,height =2 , width = 6)
		self.press7Button.pack(side = LEFT)

		self.press8Button = Button(frame,text = "8",font = myFont ,command = self.press8,height =2 , width = 6)
		self.press8Button.pack(side = LEFT)

		self.exitButton = Button(frame,text = "Close",font = myFont ,command = self.exit,height =2, width = 6)
		self.exitButton.pack(side = LEFT)
		

	def press1(self):
		ser.write('1')
		tkMessageBox.showinfo("Press","Please Press Close to deposit the books")
	def press2(self):
		ser.write('2')
		tkMessageBox.showinfo("Press","Please Press Close to deposit the books")
	def press3(self):
		ser.write('3')
		tkMessageBox.showinfo("Press","Please Press Close to deposit the books")
	def press4(self):
		ser.write('4')
		tkMessageBox.showinfo("Press","Please Press Close to deposit the books")
	def press5(self):
		ser.write('5')        																		#FUNCTION DEFINITION
		tkMessageBox.showinfo("Press","Please Press Close to deposit the books")
	def press6(self):
		ser.write('6')
		tkMessageBox.showinfo("Press","Please Press Close to deposit the books")
	def press7(self):
		ser.write('7')
		tkMessageBox.showinfo("Press","Please Press Close to deposit the books")
	def press8(self):
		ser.write('8')
		tkMessageBox.showinfo("Press","Please Press Close to deposit the books")
	def printm(self):
		tkMessageBox.showinfo("ABOUT NITC LIBRARY AUTOMATIC ISSUE PROCESS", "NITC AUTOMATIC LIBRARY RETURN SYSTEM WAS DEVELOPED BY A GROUP OF MECHANICAL ENGINEERING STUDENTS. \n NAMES: \n B.R.GURUTEJA \n G.VIJAY VAMSI \n OTHERS")
	def exit(self):
		ser.write('9')
		tkMessageBox.showinfo(" LOAD", " SCANNING ")
		delay = 10000
		print ser.readline()
		tkMessageBox.showinfo("CHECK IN ", "BOOKS \n 1. THEORY OF MACHINES BY S.S.RATTAN")
		tkMessageBox.showinfo("DIALOGUE"," UNPAID LIBRARY CHARGES= xxxxx")
		answer = tkMessageBox.askquestion("Payment","Do you want to clear the dues")
		if answer == "yes":
			tkMessageBox.showinfo("..PAYMENT..","Please Swipe your Debit/Credit Card in the Swiping Machine")
			tkMessageBox.showinfo("..."," Processing....")
			tkMessageBox.showinfo("DETAILS"," YOUR CURRENT CHECKOUTS :\n 1. Theory of Machines by S.S. Rattan \n 2. Introduction to Robotics by Craig \n 3. Control Systems by Ogata")
			tkMessageBox.showinfo("DETAILS"," You have returned these books:\n 1. Mechanics of Machinery \n 2. Dynamics of Machinery ")
			tkMessageBox.showinfo("...","THANK YOU")
		if answer == "no":
			tkMessageBox.showinfo("..."," Processing....")
			tkMessageBox.showinfo("DETAILS"," ITEMS OVERDUE :\n 1.Theory of Machines by S.S. Rattan \n 2. Introduction to Robotics by Craig \n 3. Control Systems by Ogata")
			tkMessageBox.showinfo("DETAILS"," You have returned these books:\n 1. Mechanics of Machinery \n 2. Dynamics of Machinery ")
			tkMessageBox.showinfo("...","YOU HAVE ITEMS IN OVERDUE")
			tkMessageBox.showinfo("WARNING","Dues must be cleared for issue of books")

			


root = Tk()
root.title(" CENTRAL LIBRARY NATIONAL INSTITUTE OF TECHNOLOGY, CALICUT")
root.geometry('800x480')
myFont1 = tkFont.Font(family = 'Helvetica', size = 16, weight = 'bold')
myFont = tkFont.Font(family = 'Helvetica', size = 12, weight = 'bold')
photo = PhotoImage(file = "~/Music/nitl.png")                            # IMAGE  FILE PATH 
status = Label(root, text = "Press the respective number for returning the same number of books " , font = myFont ,bd =1 , relief = SUNKEN, anchor = S)
status.pack(side = BOTTOM)
label = Label(root,image=photo)
label.pack()
b = nitc(root)
root.mainloop()
