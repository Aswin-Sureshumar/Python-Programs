list=[]
list1=[]
cf=[]
print(" enter the numbers for which the gcd is to calculated ") 
a=int(input())
b=int(input())
for i in range(1,a+1):
    if a%i==0:
        list.append(i)
print(" factors of %d are "%(a),list)
for j in range(1,b+1):
    if b%j==0:
        list1.append(j)
print(" factors of %d are "%(b),list1)
for i in list:
    if i in list1:
        cf.append(i)
print(" the gcd of %d and %d is %d"%(a,b,cf[-1]))