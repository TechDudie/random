import random
# a = 38563919364836273485827934683747283748362946584658264857384729485629475629485636287498385638294658374728019182084730719384659381628749484628637352761838452629573518385638293846338563936593846295758365
e=int
f=range
p=print
h="This number is "
j="random."
k=f"not {j}"
a=random.randint(e("1"+"0"*199),e("9"*200))
a=str(a)
a=''.join([g*2 for g in a])
a=a[1:-1]
a=[a[i:i + 2] for i in f(0,len(a),2)]
x=0
for i in a:
    a[x]=e(i)
    x+=1
b=[]
for i in f(0,100):b.append(0)
for i in a:b[i-1]+=1
c=0
for i in b:
    if i>5:c+=i-5
z=0
o=0
for i in b:
    if i==0:z+=1
    if i==1:o+=1
d=0
if c>=7:d+=1
if z>=17:d+=1
if o<=20:d+=1
if d>=2:p(f"{h}{k}")
else:
    if c>=7:p(f"{h}probably {k}")
    else:p(f"{h}{j}")
