def factor(a):
    list=[]
    for i in range(1,a+1):
        if a%i==0:
            list.append(i)
    print(" factors of %d are "%(a),list)
a=int(input(" enter the number "))
factor(a)