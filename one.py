from tkinter import *
from PIL import Image , ImageTk #for adding photo  in the jpg form


def click(event):
    global Scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        pass
    elif text == "C":
        pass
    else:
        Scvalue.set(Scvalue.get() + text)
        Screen.update()



page_root=Tk()

page_root.geometry("777x555") #for the size of the page 
# page_root.maxsize(700,390) #for setting  the  Maxsize of the page 
# page_root.minsize(333,333) #for settiing  the Minsize of the page 


mohit=Label(text="CALCULATOR" ,font="Verdana 40 bold") #heading for the page 
mohit.pack()


Scvalue=StringVar()
Scvalue.set("")
Screen=Entry(page_root ,textvar=Scvalue , font=" Courier 35 bold")
Screen.pack()

f=Frame(page_root,bg="gray")

b=Button(f,text=9,padx=15,pady=18,font="Courier 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)


b=Button(f,text=8,padx=15,pady=18,font="Courier 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b=Button(f,text=7,padx=15,pady=18,font="Courier 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()


f=Frame(page_root,bg="gray")

b=Button(f,text=6,padx=15,pady=18,font="Courier 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)


b=Button(f,text=5,padx=15,pady=18,font="Courier 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b=Button(f,text=4,padx=15,pady=18,font="Courier 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)



f.pack()

f=Frame(page_root,bg="gray")

b=Button(f,text=3,padx=15,pady=18,font="Courier 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)


b=Button(f,text=2,padx=15,pady=18,font="Courier 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b=Button(f,text=1,padx=15,pady=18,font="Courier 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)



f.pack()
page_root.mainloop()
