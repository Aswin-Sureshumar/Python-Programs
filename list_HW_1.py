a=int(input(" Enter the number of elements : "))
list=[]
greater=[]
smaller=[]
print(" Enter the list elements : ")
for i in range(a):
	b=int(input())
	list.append(b)
print(" list : ",list)
c=int(input(" Enter the number to be searched "))
if c in list:
    for i in list:
        if i>=c:
            greater.append(i)
        else:
            smaller.append(i)
    print(" Greater : ",greater,"\n Smaller : ",smaller)
else:
    print(" The entered number is not in the list. Enter another number")