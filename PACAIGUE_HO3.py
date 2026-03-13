

import tkinter as tk
window = tk.Tk()
window.title("Pacaigue_HO3")
window.configure(bg="purple")

window.resizable(False,False)

label=tk.Label(window,text="calculator")
label.grid(row=0, column=0, columnspan=2, pady=10)

frame=tk.Frame(window,bg="blue")
frame.grid(padx=5,pady=10,columnspan=5)

labell=tk.Label(window,text="Enter 1st number:")
labell.grid(row=1, column=0, padx=5, pady=5)



entry=tk.Entry(window,width=10)
entry.grid(row=1, column=1,pady=10,padx=10)

entry1=tk.Entry(window,width=10)
entry1.grid(row=2, column=1,pady=10,padx=10)

labell=tk.Label(window,text="Enter 2nd number:")
labell.grid(row=2, column=0, padx=5, pady=5)

def add():
    add1=int(entry.get())
    add2=int(entry1.get())
    add3=add1+add2
    label["text"]=f"the sum of {add1} + {add2} is {add3}."

button=tk.Button(window,text="add",command=add,state="normal")
button.grid(row=3,column=0)

def subtract():
    add1=int(entry.get())
    add2=int(entry1.get())
    add3=add1-add2
    label["text"]=f"the sum of {add1} - {add2} is {add3}."

button=tk.Button(window,text="subtract",command=subtract,state="normal")
button.grid(row=3,column=1,columnspan=1)

def multiply():
    add1=int(entry.get())
    add2=int(entry1.get())
    add3=add1*add2
    label["text"]=f"the sum of {add1} * {add2} is {add3}."

button=tk.Button(window,text="multiply",command=multiply,state="normal")
button.grid(row=4,column=0)


def division():
    add1=int(entry.get())
    add2=int(entry1.get())
    add3=add1/add2
    label["text"]=f"the sum of {add1} / {add2} is {add3}."

button=tk.Button(window,text="division",command=division,state="normal")
button.grid(row=4,column=1)

window.mainloop()
