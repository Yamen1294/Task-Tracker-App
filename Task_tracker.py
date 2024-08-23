import tkinter as tk
from tkinter import *
from tkinter import messagebox
#----------functions----------#
def add_task():
    task= task_entry.get()
    if task:
        task_listbox.insert(tk.END,task)
        task_entry.delete(0,tk.END)
    else:
        messagebox.showerror('input error','Add a task input isnot variable ')
        
def remove_task():
    try:
        selected_item = task_listbox.curselection()[0]
        task_listbox.delete(selected_item)
    except IndexError:
        messagebox.showwarning('selection error','Please selecte a task to remove.')


def clear_tasks():
    task_listbox.delete(0,tk.END)
    
#colors

color1 = '#020f12'
color2 = '#05d7ff'
color3 = '#65e7ff'
color4 = 'black'

#----------Window----------#
root = tk.Tk()
root.geometry('790x590')
root.resizable(False,False)
root.title("Task Tracker App")
root.config(bg=color1)



label = tk.Label(
    root,
    text=('Task Track App'),
    font=('Arial',14,'bold'),
    fg='white',
    bg=color1
)
label.pack(pady=0.5)
#----------Frame----------#
fram= tk.Frame(root,bg='white')
fram.pack(pady = 10, padx = 10)

#----------Entry----------#
task_entry= tk.Entry(fram,width=40,bg='white')
task_entry.pack(side= tk.LEFT, padx= 10)

#----------add button----------#
add_button = tk.Button(fram,text="Add Task",command=add_task,
                       bg=color2,
                       foreground=color4,
                       activebackground=color3,
                       activeforeground=color4,
                       highlightthickness=2,
                       highlightbackground=color2,
                       highlightcolor='white',
                       border=0,
                       cursor='hand1')
add_button.pack(side= tk.LEFT)

#----------List box ----------#

task_listbox = tk.Listbox(root,width=90,height=20)
task_listbox.pack(pady=10)

#----------Remove----------#

remove_button = tk.Button(root,text="Remove Task",command=remove_task,
                          #fg='red',
                          #bg='black')
                          bg=color1,
                       foreground=color2,
                       activebackground='red',
                       activeforeground=color4,
                       highlightthickness=2,
                       highlightbackground=color2,
                       highlightcolor='white',
                       border=0,
                       cursor='hand1')
remove_button.pack(pady=5)

#----------Clear----------#
clear_button = tk.Button(root,
                         text="Clear Tasks",
                         command=clear_tasks,
                         bg=color1,
                       foreground=color2,
                       activebackground='red',
                       activeforeground=color4,
                       highlightthickness=2,
                       highlightbackground=color2,
                       highlightcolor='white',
                       border=0,
                       cursor='hand1')

clear_button.pack(pady=5)

#def bt1_enter(event):
    #remove_button.config(
    #    highlightbackground=color3
   # )
    
#def bt1_leave(event):
 #   remove_button.config(
  #      highlightbackground=color3
   # )
    
#remove_button.bind('<Enter>',bt1_enter)
#remove_button.bind('<Leave>',bt1_leave)

root.mainloop()