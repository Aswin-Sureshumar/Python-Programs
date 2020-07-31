sum=0
num=int(input(" enter natural number range ")) 
for i in range (1,num+1):
	sum=sum+i**2
print(' sum of square of first %d natural numbers is %d'%(num,sum))
