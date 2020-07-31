acc=[1234,12345,123456]
pas=[1234,1233,1232]
amt=[1000,2000,3000]
def password(pa,ac,a,amt):
    b=input(" Enter password : ")
    print("pa",pa,"b",b)
    if b in pa:
        print("b exists")
    elif b not in pa:
        print("b no")
    # if b in pa:
        # i=pa.index(b)
        # if ac.index(i)==a:
            # c=choice()
            # if c==1:
                # d=withdraw(pa,ac,a,amt,i)           
            # elif c==2:
                # bal(amt,i)
    # else:
        # print(" entered password is wrong : ")
        # ch=choice()
        # if ch==1:
            # create()
def create():
    a=input(" Enter new password : ")
    print(" Minimum balance is 500 ")
    return(a)
def withdraw(pa,ac,a,amt,i):
    a=input(" Enter the amt to withdraw : ")
    b=amt.index(i)
    if a<b and b-a>500:
        c=b-a
    return(c)
def bal(amt,i):
    print(" The balance is : ",amt(i))
def choice():
    c=int(input(" Enter choice : "))
    return c
a=int(input(" Enter the account number : "))
if a in acc:
	c=password(pas,acc,a,amt)
	pas.append(c)
else :
	acc.append(a)
	b=create()
	pas.append(b)
print(pas,acc)