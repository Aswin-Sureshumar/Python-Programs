list=[1,2,3,4,5,6,7,8,9,0]
n=int(input(" enter the number to be checked "))
print(" number of elements in the list is %d"%len(list))
list.count(n)
if list.count==0:
    print(" the number %d is not present"%n)
else:
    print(" the number %d is present"%n)