sudo apt install python3.11-fullfrom tkinter import *

root = Tk()

my_name = StringVar()


def show_Name():
    my_name.set('sian pirzadeh')


# Page settings
root.title('E App')
root.geometry('250x300')
root.resizable(width=False, height=False)
color = 'yellow'
root.configure(bg=color)

# Frames ==>
top_first = Frame(root, width=250, height=50, bg='red')
top_first.pack(side=TOP)

# labels ==>
label = Label(root, text='show my Name : ', textvariable=my_name)
label.place(x=70, y=40)

# Button's ==>
btn = Button(root, text='Enter', command=lambda: show_Name())
btn.place(x=75, y=90)

# Entry ==>
inputTxt = Entry(root)
inputTxt.place(x=70, y=70)

def get_name():
    print(inputTxt.get())


btn_1 = Button(root, text='Show Name in console', command=lambda: get_name())
btn_1.place(x=70, y=120)

root.mainloop()
