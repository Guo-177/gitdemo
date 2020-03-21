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
