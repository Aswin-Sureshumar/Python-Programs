sum=0
num=int(input(" enter natural number range ")) 
for i in range (1,num+1):
	sum=sum+i**3
print(' sum of cubes of first %d natural numbers is %d'%(num,sum))
