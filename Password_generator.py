from tkinter import *
import random
import tkinter.messagebox as tmsg
import pyperclip

def pro():
 lst="abcdefghijklmnsopurstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567891!@#$%^&*_+-?"
 n=s_val.get()
 ran=random.sample(lst,n)
 r_val.set(ran)
 lab.update()

def copy():
 str=''
 r=r_val.get()
 for item in r:
  if item!="'" and item!="," and item!="(" and item!=")" and item!=" ":
   str = str+item
 pyperclip.copy(str) 
 tmsg.showinfo("Response","Copied to clipboard")


root=Tk()

root.geometry("650x440")
root.wm_maxsize(650,440)
root.wm_minsize(650,440)
root.title("PASSWORD MAKER")
root.configure(background="gray19")

s_val=IntVar()
r_val=StringVar()


input=Entry(root,textvariable=s_val,bg="ghost white",justify="center",width=5)
input.place(x=230,y=173)

b=Button(root,text="GENERATE",bg="DeepSkyBlue1",command=pro)
b.place(x=515,y=75)

b2=Button(root,text="copy",relief="flat",command=copy)
b2.place(x=470,y=75)

lab=Label(root,textvariable=r_val,bd=10,relief="raised",bg="ghost white",anchor="w")
lab.place(x=70,y=70,width=400)

Label(root,text="Length of password",fg="white",bg="gray19",font="Bold 12").place(x=70,y=170)



root.mainloop()

