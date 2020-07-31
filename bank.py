acc=123456
pin=1234
bal=12345
a=int(input(" enter the account number : "))
b=int(input(" enter the pin number : "))
if a==acc and b==pin:
    choice=int(input(" enter the choice : "))
    if choice==1:
        print(" account balance : ",bal)
    elif choice==2:
        dep=int(input(" enter the deposit amt : "))
        bal=bal+dep
        print( " new balance is : ",bal)
    elif choice==3:
        wd=int(input(" enter the withdrawal amount : "))
        bal=bal-wd
        print(" new balance is : ",bal)
elif a!=acc and b==pin:
    print(" enter correct account number ")
elif a==acc and b!=pin:
    print(" enter correct pin number ")
elif a!=acc and b!=pin:
    print(" enter correct credentials ")