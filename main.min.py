import random as O
# a = 38563919364836273485827934683747283748362946584658264857384729485629475629485636287498385638294658374728019182084730719384659381628749484628637352761838452629573518385638293846338563936593846295758365
E=int
I=range
F=print
G='This number is '
J='random.'
K=f"not {J}"
A=O.randint(E('1'+'0'*199),E('9'*200))
A=str(A)
A=''.join([B*2 for B in A])
A=A[1:-1]
A=[A[B:B+2]for B in I(0,len(A),2)]
L=0
for B in A:A[L]=E(B);L+=1
C=[]
for B in I(0,100):C.append(0)
for B in A:C[B-1]+=1
H=0
for B in C:
	if B>5:H+=B-5
M=0
N=0
for B in C:
	if B==0:M+=1
	if B==1:N+=1
D=0
if H>=7:D+=1
if M>=17:D+=1
if N<=20:D+=1
if D>=2:F(f"{G}{K}")
elif H>=7:F(f"{G}probably {K}")
else:F(f"{G}{J}")
