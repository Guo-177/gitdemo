f=open('d:\duanwen.txt','r')
a=f.read()
m=a[:]
a=a.lower()
a=a.split()
for i in a:
    if i==','or i=='.' or i=='!' or i=='?':
        a.remove(i)
print(a)
print('总数:',len(a))
b=set(a)
d=[]
x={}
y={}
k=[]
l=[]
for i in b:
    print(i,':',a.count(i))
    y[i]=a.count(i)
t=open('d:\\tingyong.txt','r')
c=t.read()
c=c.split()
for i in a:
    if i not in c:
        d.append(i)
e=set(d)
for i in e:
    print('停用',i,':',d.count(i))
    x[i]=d.count(i)
g=x.values()
g=list(g)
h=x.keys()
h=list(h)
for i in range(6):
    j=g.index(max(g))
    print(h[j],max(g))
    k.append(h[j])
    l.append(max(g))
    g.remove(max(g))
    h.remove(h[j])
from tkinter import *
top=Tk()
top.geometry('300x200')
top.title('文本编辑器')
def showoff():
    root1=Tk()
    root1.geometry('1000x200')
    root1.title('文本')
    label1=Label(root1,text=m,wraplength=1000)
    label1.pack()
    root1.mainloop()
def statistics1():
    root2=Tk()
    root2.geometry('300x200')
    root2.title('总单词个数')
    label2=Label(root2,text=len(a))
    label2.pack()
    root2.mainloop()                 
def statistics2():
    root3=Tk()
    root3.geometry('1000x200')
    root3.title('词频统计')
    label3=Label(root3,text=y,wraplength=1000)
    label3.pack()
    root3.mainloop()
    def keyword():
    import matplotlib.pyplot as plt
    import numpy as np
    plt.bar(range(len(l)),l,tick_label=k)
    plt.title('the words that are used the most often')             
    plt.show()
button1=Button(top,text='显示文本',command=showoff)
button2=Button(top,text='总单词个数统计',command=statistics1)
button3=Button(top,text='词频统计',command=statistics2)
button4=Button(top,text='关键词',command=keyword)
button5=Button(top,text='退出',command=quit)
button1.grid_configure(column=1,row=1,columnspan=1,rowspan=1)
button2.grid_configure(column=1,row=3,columnspan=1,rowspan=1)
button3.grid_configure(column=1,row=5,columnspan=1,rowspan=1)
button4.grid_configure(column=1,row=7,columnspan=1,rowspan=1)
button5.grid_configure(column=1,row=9,columnspan=1,rowspan=1)
top.mainloop()



