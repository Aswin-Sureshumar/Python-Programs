list=[1,2,3,4,5,6,7,8,9]
list1=[]
list2=[]
list3=[]
for i in list:
	if i%2==0:
		list1.append(i)
	elif i%2!=0:
		list2.append(i)
print(" the even numbers are",list1)
print(" the odd numbers are",list2)
for i in list:
    if list.index(i)%i==0:
        break
    else:
        list3.append(i)
print(" the prime numbers are",list3)