for num in range(10,20):
    for i in range(2,num):
        if num%2==0:
            j=num/i
            print('\n %d equals %d * %d'% (num,i,j))
            break
    else:
            print("\n\tit is a prime number")