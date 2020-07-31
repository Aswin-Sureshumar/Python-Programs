list=[1,2,5,4,-5,-3,0]
count=0
count1=0
for i in list:
	if i>=0:
		count+=1
	else:
		count1+=1
print(" number of positive num in list is %d"%count)
print(" number of negative num in list is %d"%count1)