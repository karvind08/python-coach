from tkinter import *
window = Tk()
window.title('Geometry')
window.geometry('400x500')
window.minsize(300, 300)
window.maxsize(600, 600)
window.iconbitmap(
    r'C:\Users\Arvind\Desktop\Pandas\APP-2022\Event Handling\fav.ico')
l1 = Label(window, text='My Button: ').grid(column=0, row=1)
entry = Entry(window, width=50).grid(row=1, column=20)
window.mainloop()
