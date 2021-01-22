from tkinter import *
from math import sqrt
#0.5 and -3
#print(f"{a}x**2+({b}x)+({c})")
#D=b**2-4*a*c
#if D>0:
#    print("There are 2 roots")
#    x1=(-1*b+sqrt(D))/(2*a)
#    x2=(-1*b-sqrt(D))/(2*a)
#    print()
#    print(f"x1={x1}")
#    print(f"x2={x2}")
#elif D==0:
#    print("Roots are the same")
#    x=(-1*b)/(2*a)
#    print(f"x={x}")
#else:
#    print("There are no roots. D<0")
eqt="test"
def confirm(event):
    a=enta.get()
    b=entb.get()
    c=entc.get()

scr=Tk()
scr.title("Square Equation")
scr.geometry("600x400")
enta=Entry(scr,width=15,fg="Crimson",font="Comic_Sans 16",bd=10)
entb=Entry(scr,width=15,fg="Crimson",font="Comic_Sans 16",bd=10)
entc=Entry(scr,width=15,fg="Crimson",font="Comic_Sans 16",bd=10)
btn=Button(scr,text="Confirm")

#img=PhotoImage(file="Ivara Prime Access.png").subsample(5)
lbl=Label(scr,bg="gray",fg="crimson",bd=10,anchor=NW,text="something",font="Ariel 16")

btn.bind("<Button-1>",confirm)
enta.grid(column=0,row=0)
entb.grid(column=0,row=1)
entc.grid(column=0,row=2)
lbl.grid(column=0,row=3)

scr.mainloop()
#import os
#os.remove(filename)
#fig.savefig("graph.png")