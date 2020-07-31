class Student:
    count=0
    name=[]
    roll=[]
    age=[]
    gender=[]
    def __init__(self,name,roll,age,gender):
        Student.name.append(name)
        Student.roll.append(roll)
        Student.age.append(age)
        Student.gender.append(gender)
        Student.count+=1
    def displaystudent(self):
        for i in range(Student.count):
            print("\n Name : ",self.name[i])
            print("\n Roll No : ",self.roll[i])
            print("\n Age : ",self.age[i])
            print("\n Gender : ",self.gender[i])
a= int(input(" Enter the number of students "))
for i in range(a):
    a,b,c,d=map(str,input().split(" "))
    s=Student(a,b,c,d)
Student.displaystudent(s)