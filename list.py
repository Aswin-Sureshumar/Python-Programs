list3=[1,2,6,7,8];
list1=[2,3,4,5]
print("list[3]= ",list3[3])
print("list[1:3]",list3[0:3])
list3[1]=3;
print("updated list",list3)
del list3[2]
print("delete a",list3)
len(list3)
print("length of list",len(list3))
list2=list3+list1
print("list2= ",list2)
print(list1*4)
for i in list3:
    print(i,end="")
print ("\n",max(list3))
print ("\n",min(list3))
tuple=(1,2,3,3,5)
alist=list(tuple)
print(alist)