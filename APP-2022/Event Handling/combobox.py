from tkinter import *
from tkinter import ttk
window = Tk()
window.title('Geometry')
window.geometry('400x500')
window.minsize(300, 300)
window.maxsize(600, 600)
window.iconbitmap(
    r'C:\Users\Arvind\Desktop\Pandas\APP-2022\Event Handling\fav.ico')
cb = ttk.Combobox(window, values=[1, 2, 3, 4])
cb.current(1)
cb.grid(row=1, column=5)
window.mainloop()
