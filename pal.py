def palindrome(a):
    for i in range(0,l//2):
        if a[i]!=a[l-i-1]:
            return 0
        else:
            return 1
str="malayalam"
l=len(str)
pal=palindrome(str)
if pal==1:
    print( " %s is a palindrome "%(str))
else:
    print( " %s is not a palindrome "%(str))