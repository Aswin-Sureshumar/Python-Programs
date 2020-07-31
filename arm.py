a=int(input(" Enter the interval "))
b=0
c=a
for i in range (1,a):
    while i>0:
        arm=a%10
        b=b+arm**3
        a=int(a/10)
    if c==b:
        print(" the number is a armstrong num ")
    else:
        print(" the number is not a armstrong num ")