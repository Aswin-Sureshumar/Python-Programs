a=int(input("\tEnter the number"))
for num in range(2,a):
    if  a%num==0:
        print(" %d is not a prime number"%(a))
        break
else:
    print("%d is a prime number"%(a))