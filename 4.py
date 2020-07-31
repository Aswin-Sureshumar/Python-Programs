class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=cal(a,b)
ch=0
print("1. Add")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
ch=int(input("Enter choice: "))
if ch==1:
    print("Result : ",c.add())
elif ch==2:
    print("Result : ",c.sub())
elif ch==3:
    print("Result : ",c.mul())
elif ch==4:
    print("Result : ",c.div())
elif ch==5:
    print("Exit")
else:
    print(" Enter Choice Between 1 to 5")