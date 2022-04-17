from tkinter import *
window = Tk()
window.title('Geometry')
window.geometry('400x500')
window.minsize(300, 300)
window.maxsize(600, 600)
window.iconbitmap(
    r'C:\Users\Arvind\Desktop\Pandas\APP-2022\Event Handling\fav.ico')
l1 = Label(window, text='Hello', fg='yellow',
           bg='black', padx=100, pady=20, font=('Arial Black', 20), relief=SUNKEN).pack()
window.mainloop()
