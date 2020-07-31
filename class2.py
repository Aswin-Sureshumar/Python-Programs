import numpy as np
a=int(input(" Enter the number of students : "))
s=[]
for i in range(a):
    for j in range(4):
            c=input()
            s.append(c)

S=np.array(s).reshape(a,4)
print(S)