from tkinter import *
from tkinter import messagebox

def newtask():
    task =my_entry.get()
    if task !='':
        lb.insert(END, task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("Warning!!","Please enter some task")


def deletetask():
    lb.delete(ANCHOR)


root = Tk()
root.geometry('500x450+500+200')
root.title("Own todo list")
root.config(bg='#223441')
root.resizable(width=False,height=False)

frame = Frame(root)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times',18),
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
lb.pack(side=LEFT,fill=BOTH)


task_list = [
    'internship' ,
    'todo list' ,
    'password generator' ,
    'simple calci' ,
    'contact book' ,
    'rps game' ,
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(root, font=('times',24))
my_entry.pack(pady=20)


button_frame = Frame(root)
button_frame.pack(pady=20)

addtask_button =Button(button_frame,  text='Add task',font=('times',24),bg='#c5f776',padx=20,pady=10,command=newtask)
addtask_button.pack(fill=BOTH, expand=True, side=LEFT)

deltask_button =Button(button_frame,text='Delete task',font=('times',24),bg='#ff8b61',padx=20,pady=10,command=deletetask)
deltask_button.pack(fill=BOTH, expand=True, side=LEFT)



root.mainloop()
