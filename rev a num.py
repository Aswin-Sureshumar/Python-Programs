a=int(input(" enter a number "))
rev=0
while a!=0:
    c=a%10
    rev=rev*10+c
    a=a//10
print("the reverse of  is ",rev)