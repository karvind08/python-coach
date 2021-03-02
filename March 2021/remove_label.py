from tkinter import *
window = Tk()
window.title('Config')
window.geometry('400x400')

def myDelete():
	#myLabel.pack_forget()
	myLabel.destroy()

def myClick():
	global myLabel
	hello = 'Hello' + e.get()
	myLabel = Label(window,text=hello)
	e.delete(0,'end')
	myLabel.pack(pady=10)

e = Entry(window,width=50,font='Helvetica 30').pack(padx=10,pady=10)

myButton = Button(window,text='Enter your Name:',command=myClick).pack(pady=10)
DeleteButton = Button(window,text='Delete Text',command=myDelete).pack(pady=10)

window.mainloop()