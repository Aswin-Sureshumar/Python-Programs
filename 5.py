list=[]
b=0
a=int(input(" Enter a number : "))
for i in range(1,11):
	if i==1:
		list.append(a)
	else:
		b=a*a
		list.append(b)
c=tuple(list)
print(" The tuple with first number as the given number and rest are square of the given is ",c)