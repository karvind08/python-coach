from tkinter import *
window = Tk()
window.title('List Box')
window.geometry('400x500')
window.minsize(300, 300)
window.maxsize(600, 600)
window.iconbitmap(
    r'C:\Users\Arvind\Desktop\Pandas\APP-2022\Event Handling\fav.ico')
lb = Listbox(window)
lb.pack()
lb.insert(END, 'This is first Item')
lb.insert(END, 'This is Second Item')
window.mainloop()
