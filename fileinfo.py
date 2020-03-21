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
