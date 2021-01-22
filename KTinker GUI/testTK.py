from tkinter import *
count=0
def pkm(event):
    global count
    count+=1
    lbl.configure(text=count,font=f"Arial {12+count}")
def clk(event):
    global count
    count+=1
    btn["text"]=str(count)
def something(event):
    t=ent.get()
    lbl.configure(text=t)
    ent.delete(0,END)
def to_ent():
    t=var.get()
    ent.delete(0,END)
    ent.insert(END,t)
win=Tk()
win.title("This is a menu")
win.geometry("600x400")

btn=Button(win,text="Click \nthis",fg="purple",bg="black",font="Times_New_Roman 14",width=10,relief=GROOVE)#SUNKEN, GROOVE, RAISED
lbl=Label(win,text="HELLO",fg="Crimson",bg="Gray",font="Arial 14",width=5,height=4)
ent=Entry(win,width=15,fg="ForestGreen",font="Comic_Sans 16",bd=10)

img=PhotoImage(file="Ivara Prime Access.png").subsample(5) #r"" find a file in the project that might be in a different folder
btn_image=Button(win,image=img)

var=IntVar() #StringVar()
var.set(3)
r1=Radiobutton(win,text="one",variable=var,value=1,command=to_ent)
r2=Radiobutton(win,text="two",variable=var,value=2,command=to_ent)
r3=Radiobutton(win,text="three",variable=var,value=3,command=to_ent)

btn.bind("<Button-1>",clk)
lbl.bind("<Button-3>",pkm)
ent.bind("<Return>",something)

#ent.pack()
#btn.pack(fill=BOTH)
#lbl.pack()
btn_image.grid(row=1,column=0)
r1.grid(row=0,column=0)
r2.grid(row=0,column=1)
r3.grid(row=0,column=2)
win.mainloop()