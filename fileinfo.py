f=open('d:\duanwen.txt','r')
a=f.read()
m=a[:]
a=a.lower()
a=a.split()
for i in a:
    if i==','or i=='.' or i=='!' or i=='?':
        a.remove(i)
print(a)
