def marklist(name,mat,eng,tamil,sci,ss):
    tot=mat+eng+tamil+sci+ss
    avg=tot/5
    print(" name: ",name)
    print(" the total is ",tot)
    print(" the avg is ",avg)
a=input(" enter name ")
b=int(input(" mat mark "))
c=int(input(" eng mark "))
d=int(input(" tamil mark "))
e=int(input(" sci mark "))
f=int(input(" ss mark "))
marklist(a,b,c,d,e,f)