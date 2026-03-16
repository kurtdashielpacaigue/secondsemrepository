import tkinter as tk
window=tk.Tk()
window.title("Profile builder")
window.configure(bg="purple")
window.geometry("700x300")

label1=tk.Label(window,text="Profile Builder")
label1.pack(side="top")

label=tk.Label(window,background="Blue",height=200,relief="raised")
label.pack(anchor="center",pady=10,padx=20,fill="both")

name_entry=tk.Entry(label,width=30)
name_entry.grid(row=1,column=0,columnspan=3,rowspan=4,padx=10)

labelname=tk.Label(label,text="First Name")
labelname.grid(row=5,column=0,padx=10,pady=10,columnspan=3,rowspan=4)

midname_entry=tk.Entry(label,width=30)
midname_entry.grid(row=1,column=6,columnspan=3,rowspan=4,padx=10)

labelname=tk.Label(label,text="Middle Name")
labelname.grid(row=5,column=6,padx=10,pady=10,columnspan=3,rowspan=4)

lastname_entry=tk.Entry(label,width=30)
lastname_entry.grid(row=1,column=12,columnspan=3,rowspan=4,padx=10)

labelname=tk.Label(label,text="Last Name")
labelname.grid(row=5,column=12,padx=10,pady=10,columnspan=3,rowspan=4)

birthyear_entry=tk.Entry(label,width=30)
birthyear_entry.grid(row=12,column=0,columnspan=3,rowspan=4,padx=10)

labelname=tk.Label(label,text="Birth Year")
labelname.grid(row=16,column=0,padx=10,pady=10,columnspan=3,rowspan=4)

labelname=tk.Label(label,text="Gender")
labelname.grid(row=24,column=0,padx=10,pady=10,columnspan=3,rowspan=4)

Gender=tk.Radiobutton(label,text="male,",bg="blue")
Gender.grid(row=24,column=5,padx=10,pady=10,columnspan=3,rowspan=4)

Gender1=tk.Radiobutton(label,text="female,",bg="blue")
Gender1.grid(row=24,column=8,padx=10,pady=10,columnspan=3,rowspan=4)


button=tk.Button(window,text="Submit",anchor="s")
button.pack()
window.mainloop()
