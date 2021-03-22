from tkinter import *
window = Tk()
window.title('Images Buttons')
login_btn = PhotoImage(file=r"C:\Users\ARVIND\Desktop\Desk\Bevy\login.png")
img_label =Label(window,image=login_btn)
img_label.pack()

def thing():
	my_label.config(text='You clicked the button')
	

my_label = Label(window,text=' ')
my_label.pack(pady=20)

window.geometry('700x500')
window.mainloop()

