from tkinter import *
window = Tk()
window.title('Geometry')
window.geometry('400x500')
window.minsize(300, 300)
window.maxsize(600, 600)
window.iconbitmap(
    r'C:\Users\Arvind\Desktop\Pandas\APP-2022\Event Handling\fav.ico')
rb1 = Radiobutton(window, text='Python', value=1).pack()
window.mainloop()
