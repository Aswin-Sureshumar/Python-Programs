a=int(input(" n term fibonacci series "))
b=0
c=1
while b<=a:
    print(" %d "%b,end=" ")
    next=b+c
    b=c
    c=next