from tkinter import *
from tkinter import colorchooser

window = Tk()
window.title('Color Picker')
window.geometry('400x300')

# 1 my_color = colorchooser.askcolor()

# 2. def color():
#	my_color = colorchooser.askcolor()

#my_button = Button(window,text='Click Me',command=color)	
#my_button.pack(pady=20)

# 3. Now Returns a color 
#def color():
#	my_color = colorchooser.askcolor()
#	my_label = Label(window,text=my_color).pack()

#my_button = Button(window,text='Click Me',command=color)	
#my_button.pack(pady=20)

# Returning hex code

#def color():
#	my_color = colorchooser.askcolor()[1]
#	my_label = Label(window,text=my_color).pack()
	
#my_button = Button(window,text='Click Me',command=color)	
#my_button.pack(pady=20)


def color():
	my_color = colorchooser.askcolor()[1]
	my_label = Label(window,text=my_color).pack()
	my_label2 = Label(window,text='You Picked a color',font='Helvetica 30 bold',bg=my_color).pack()
	
my_button = Button(window,text='Click Me',command=color)	
my_button.pack(pady=20)



window.mainloop()