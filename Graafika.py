from tkinter import *
k=0

def valik():
    val=var.get()
    ent.insert(END,val)

def klikker(event):
    global k
    k+=1
    btn.configure(text=k)
    if k==100:
        k=0
    if k%2==0:
        tahvel.itemconfig(img_kast,image=img1)
    else:
        tahvel.itemconfig(img_kast,image=img)

def klikkermaha(event):
    global k
    k-=1
    btn.configure(text=k)

def tekst_to_lbl(event):
    t=ent.get()
    lbl.configure(text=t)
    ent.delete(0,END)

def checklist_to_l(event):
    v1=var1.get()
    v2=var2.get()
    jarjend=[v1,v2]
    l.delete(0,1) # read
    for item in jarjend:
        l.insert(END,item)

aken=Tk()
aken.title("Minu esimene aken")
aken.iconbitmap("kot.ico") #ICO
f=Frame(aken,bg="magenta")
#aken.geometry("400x500")

lbl=Label(f,text="Elemendid",bg="gold",fg="#AA4A44",font="Arial 20",height=5,width=15)
btn=Button(f,text="Vajuta siia", font="Arial 24", relief=GROOVE, width=11) #GROOVE, SUNKEN, RAISED
ent=Entry(f, fg="blue",bg="lightblue",width=15,font="Arial 20",justify=CENTER)
var=IntVar() #StringVar()
r1=Radiobutton(f,text="Esimene",font="Algerian 20",variable=var,value=1,command=valik)
r2=Radiobutton(f,text="Teine",font="Algerian 20",variable=var,value=2,command=valik)
r3=Radiobutton(f,text="Kolmas",font="Algerian 20",variable=var,value=3,command=valik)
var1=StringVar()
var2=StringVar()
c1=Checkbutton(f, text="Esimene",font="Arial 20",variable=var1,onvalue="Esimene on valitud",offvalue="Esimene on peidetud")
c2=Checkbutton(f, text="Teine",font="Arial 20",variable=var2,onvalue="Teine on valitud",offvalue="Teine on peidetud")
l=Listbox(f,height=3,width=20)
tahvel=Canvas(aken,width=260,height=260,bg="gold")
img=PhotoImage(file="kot1.png").subsample(7)
img1=PhotoImage(file="kot3.png").subsample(7) #GIF,PNG
img_kast=tahvel.create_image(130,120,image=img) #anchor=NW
btn.bind("<Button-1>",klikker) #lkm
btn.bind("<Button-2>",checklist_to_l) #rattas
btn.bind("<Button-3>",klikkermaha) #pkm
ent.bind("<Return>", tekst_to_lbl) #Enter
lbl.pack()

c1.deselect()
c2.deselect()
ob=[lbl,btn,ent,r1,r2,r3,l,c1,c2]
for i in range(len(ob)):
    ob[i].pack()

f.grid(row=0,column=0)
tahvel.grid(row=0,column=1)
aken.mainloop() 