from tkinter import *
window = Tk()
window.title('Geometry')
window.geometry('400x500')
window.minsize(300, 300)
window.maxsize(600, 600)
window.iconbitmap(
    r'C:\Users\Arvind\Desktop\Pandas\APP-2022\Event Handling\fav.ico')


def clicker():
    l1.config(text="Now I am in clicker")


l1 = Label(window, text="I am a label")
l1.pack(pady=10)

btn = Button(window, text='Click me', command=clicker)
btn.pack()
window.mainloop()
