n=int(input("enter the number of rows needed "))
for i in range(1,n):
    for j in range(1,i+1):
        print('%d'%j,end="")
    print("")
## first half for top down pyramid
## second half for inverted pyramid
for i in range(n-2,0,-1):
    for j in range(1,i+1):
        print('%d'%j,end="")
    print("")