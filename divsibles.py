a=int(input(" enter a number : " ))
list=[]
for i in range(1,a+1):
	if a%i==0:
		list.append(i)
print(" number %d is divisible by "%a,list)