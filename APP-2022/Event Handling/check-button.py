from tkinter import *
window = Tk()
window.title('Geometry')
window.geometry('400x500')
window.minsize(300, 300)
window.maxsize(600, 600)
window.iconbitmap(
    r'C:\Users\Arvind\Desktop\Pandas\APP-2022\Event Handling\fav.ico')
chk_state = BooleanVar()
chk_state.set(True)
chk_btn = Checkbutton(window, text='Select',
                      var=chk_state).grid(row=1, column=1)
window.mainloop()
