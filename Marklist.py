a=int(input("enter english mark\t"))
b=int(input("enter maths mark\t"))
c=int(input("enter tamil mark\t"))
d=int(input("enter ss mark\t"))
e=int(input("enter sci mark\t"))
f=input("student name ")
tot=int(a+b+c+d+e)
avg=int(tot/5)
print("\t\nStudent Name=",f)
print("\nenglish = ",a)
print("\nmaths = ",b)
print("\ntamil = ",c)
print("\nss = ",d)
print("\nsci = ",e)
print("\nTotal = ",tot)
print("\nAverage = ",avg)
if a and b>30:
    print("pass")
else:
    print("fail")
if a>30 or c>30 or d>30 or e>30:
    print("p")
else:
    print("f")