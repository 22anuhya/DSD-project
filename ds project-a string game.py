'''def winner(c):
    return c%2==0
def startgame(l,string):
    count=0
    for v in range(len(l)):
        if l[v] in string:
            ind=string.index(l[v])
            count+=1
            #replace gap in place of that substring
            string=string[:ind]+' '+string[(len(l[v])+ind):]
    return string,count
s=int(input())
while s>0:
    n=input()
    x=int(input())
    l=[]
    for i in range(x):
        v=input()
        if v in n:
            l.append(v)
    n,c=startgame(l,n)
    print('Tracy') if winner(c) else print('Teddy')
    s-=1'''
from tkinter import *
from tkinter import messagebox
o=Tk()
x=" "*65
o.title(x+"A String Game")
o.geometry("600x600")
bg=PhotoImage(file="C:/Users/Anuhya/Downloads/teddy and tracy-ds project.gif")
canvas1=Canvas(o,width=500,height=500)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image(0,0,image=bg,anchor="nw")
Label(o,text='Enter string entered by tracy',bg='pink').place(x=170,y=80)
Label(o,text='Enter dictionary words',bg='pink').place(x=170,y=130)
def pri():
    global string
    string=e1.get()
    #print(string)
    Label(o,text=f'The entered string is {string}',bg='light green').place(x=230,y=230)
def dict_words():
    global l,lw
    lw=[]
    l=e2.get().split()
    for i in l:
        if i in string:
            lw.append(i)
    #print(lw)
    Label(o,text=f'Dictionary words present in given string are {lw}',bg='light green').place(x=160,y=260)
def winner():
    global string,c,lw
    c=0
    for i in lw:
        if i in string:
            ind=string.index(i)
            c+=1
            #replace gap in place of that substring
            string=string[:ind]+' '+string[(len(i)+ind):]
    #print(c)
    #print("TEDDY") if c%2==1 else print("TRACY")
    if c%2==1:
        messagebox.showinfo("RESULT","TEDDY WON :)")
    else:
        messagebox.showinfo("RESULT","TRACY WON :)") 
e1=Entry(o)
e1.place(x=330,y=80)
e2=Entry(o)
e2.place(x=330,y=130)
b1=Button(o,text="display string",bg='yellow',command=pri).place(x=440,y=80)
b2=Button(o,text="display words",bg='yellow',command=dict_words).place(x=440,y=130)
b3=Button(o,text="winner",bg='light blue',font='bold',command=winner).place(x=360,y=300)


