from tkinter import *
window = Tk()
window.title('Menu Bar')
window.geometry('400x300')
#window.iconbitmap(r'C:\Users\ARVIND\Desktop\Desk\Bevy\av.ico')
my_menu = Menu(window)
window.config(menu=my_menu)
def our_command():
    l1 = Label(window,text='You clicked the dropdown menu').pack()

#create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label='File',menu=file_menu)
#file_menu.add_command(label='New..',command=our_command)
#file_menu.add_command(label='Open',command=our_command)
#file_menu.add_command(label='Save',command=our_command)
#file_menu.add_separator()
#file_menu.add_command(label='Exit',command=window.quit)

#create edit menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label='Edit',menu=edit_menu)
#edit_menu.add_command(label='Cut',command=our_command)
#edit_menu.add_command(label='Copy',command=our_command)

find_menu = Menu(my_menu)
my_menu.add_cascade(label='Find',menu=find_menu)
#find_menu.add_command(label='Find',command=our_command)

window.mainloop()
