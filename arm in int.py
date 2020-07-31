n=int(input(" range "))
list=[]
for a in range(1,n):
    c=a
    b=0
    while a>0:
        arm=a%10
        b=b+arm**3
        a=int(a/10)
    if c==b:
        list.append(b)
print(list)