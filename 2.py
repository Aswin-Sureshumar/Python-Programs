list=[]
a=int(input(" Enter the number "))
for i in range (2,a+1):
	if a%i==0:
		list.append(i)
print(" Smallest Divisor of %d is : %d"%(a,min(list)))