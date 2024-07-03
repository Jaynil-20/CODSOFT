from tkinter import *

root=Tk()

root.geometry("450x500")
root.wm_maxsize(450,500)
root.wm_minsize(450,500)
root.configure(bg="gray19")

def Add():
    text=task.get()
    lst.insert(END,f"•{text}")
    task.set("")
    

def Del():
    lst.delete(first=0,last=END)
    

def done():
    s=lst.curselection()
    lst.delete(s)

Label(root,text="To Do List",font="Helvetica 20",bg="gray19",fg="magenta2").place(x=170,y=30)

task=StringVar()
input_dis=Entry(root,textvariable=task,width=60)
input_dis.place(x=30,y=100)

b1=Button(root,text="Add",relief="groove",bg="dark violet",bd=5,command=Add)
b1.place(x=400,y=95)

lst=Listbox(root,width=50,height=15,bg="snow2")
lst.place(x=90,y=150)

b2=Button(root,text="Delete❎",bg="red",command=Del)
b2.place(x=90,y=400)

b3=Button(root,text="Done✅",bg="green2",command=done)
b3.place(x=90,y=430)

root.mainloop()