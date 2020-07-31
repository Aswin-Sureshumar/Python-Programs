list=[]
a=int(input(" Enter the number of elements : "))
for i in range(a):
	list.append(int(input()))
print(" list : ",list)
for i in range(a):
    print(" Element popped : ",list.pop())
# list1=[]
# b=int(input(" Enter the number of elements : "))
# for i in range(b):
	# list1.append(int(input()))
# print(" list : ",list1)
# for i in range(b):
    # print(" Element popped : ",list1.pop(0))