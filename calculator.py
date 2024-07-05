from tkinter import *

root=Tk()

root.geometry("400x520")
root.wm_maxsize(400,520)
root.wm_minsize(400,520)
root.title("Calculator")
root.config(background="black")
global disply_val

def click(event):
    
   text=event.widget.cget("text")
   if(text=="="):
      if(disply.get().isdigit()):
         val=int(disply.get())

      else:
         val=eval(disply.get())
      disply_val.set(val)   

   elif(text=="C"):
       disply_val.set("")    
       disply.update()

   elif(text=="x²"):
       val=disply.get()
       val=(int(val)*int(val))
       disply_val.set(val)
       disply.update()

   elif(text=="±"):
       val=disply_val.get()
       val=(-int(val))
       disply_val.set(val)
       disply.update()

   else:
       disply_val.set(disply.get()+text)
       disply.update()

disply_val=StringVar()
disply_val.set("")

disply=Entry(textvariable=disply_val,justify="right",width=400,font="Bold 35",bg="black",fg="white")
disply.pack(fill=Y)

b1=Button(root,bg="gray15",fg="white",text="%",width=10,height=5,relief="flat",padx=10)
b1.bind("<Button-1>",click)
b1.place(x=0,y=65)
b2=Button(root,bg="gray15",fg="white",text="C",width=10,height=5,relief="flat",padx=10)
b2.bind("<Button-1>",click)
b2.place(x=100,y=65)
b3=Button(root,bg="gray15",fg="white",text="x²",width=10,height=5,relief="flat",padx=10)
b3.bind("<Button-1>",click)
b3.place(x=200,y=65)
b4=Button(root,bg="gray15",fg="white",text="/",width=10,height=5,relief="flat",padx=10)
b4.bind("<Button-1>",click)
b4.place(x=300,y=65)


b5=Button(root,bg="gray19",fg="white",text="7",width=10,height=5,relief="flat",padx=10)
b5.bind("<Button-1>",click)
b5.place(x=0,y=155)
b6=Button(root,bg="gray19",fg="white",text="8",width=10,height=5,relief="flat",padx=10)
b6.bind("<Button-1>",click)
b6.place(x=100,y=155)
b7=Button(root,bg="gray19",fg="white",text="9",width=10,height=5,relief="flat",padx=10)
b7.bind("<Button-1>",click)
b7.place(x=200,y=155)
b8=Button(root,bg="gray15",fg="white",text="*",width=10,height=5,relief="flat",padx=10)
b8.bind("<Button-1>",click)
b8.place(x=300,y=155)

b9=Button(root,bg="gray19",fg="white",text="4",width=10,height=5,relief="flat",padx=10)
b9.bind("<Button-1>",click)
b9.place(x=0,y=245)
b10=Button(root,bg="gray19",fg="white",text="5",width=10,height=5,relief="flat",padx=10)
b10.bind("<Button-1>",click)
b10.place(x=100,y=245)
b11=Button(root,bg="gray19",fg="white",text="6",width=10,height=5,relief="flat",padx=10)
b11.bind("<Button-1>",click)
b11.place(x=200,y=245)
b12=Button(root,bg="gray15",fg="white",text="-",width=10,height=5,relief="flat",padx=10)
b12.bind("<Button-1>",click)
b12.place(x=300,y=245)


b13=Button(root,bg="gray19",fg="white",text="1",width=10,height=5,relief="flat",padx=10)
b13.bind("<Button-1>",click)
b13.place(x=0,y=335)
b14=Button(root,bg="gray19",fg="white",text="2",width=10,height=5,relief="flat",padx=10)
b14.bind("<Button-1>",click)
b14.place(x=100,y=335)
b15=Button(root,bg="gray19",fg="white",text="3",width=10,height=5,relief="flat",padx=10)
b15.bind("<Button-1>",click)
b15.place(x=200,y=335)
b16=Button(root,bg="gray15",fg="white",text="+",width=10,height=5,relief="flat",padx=10)
b16.bind("<Button-1>",click)
b16.place(x=300,y=335)

b17=Button(root,bg="gray15",fg="white",text="±",width=10,height=5,relief="flat",padx=10)
b17.bind("<Button-1>",click)
b17.place(x=0,y=425)
b18=Button(root,bg="gray15",fg="white",text="0",width=10,height=5,relief="flat",padx=10)
b18.bind("<Button-1>",click)
b18.place(x=100,y=425)
b19=Button(root,bg="gray15",fg="white",text=".",width=10,height=5,relief="flat",padx=10)
b19.bind("<Button-1>",click)
b19.place(x=200,y=425)
b20=Button(root,bg="chocolate1",fg="black",text="=",width=10,height=5,relief="flat",padx=10)
b20.bind("<Button-1>",click)
b20.place(x=300,y=425)




root.mainloop()