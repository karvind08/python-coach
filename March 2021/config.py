from tkinter import *
window = Tk()
window.title('Config')
window.geometry('400x400')

def something():
	my_label.config(text='This is new text')
	window.config(bg='blue')
	#my_button.config(text='You are hero')
	my_button.config(text='You are hero',state=DISABLED)

global my_label
my_label = Label(window,text='This is old text')
my_label.pack(pady=10)

global my_button
my_button = Button(window,text='Click Me',command=something)
my_button.pack(pady=10)

window.mainloop()