def quad(a,b,c):
    x1=((-b)+((b**2-4*a*c)**0.5))/(2*a)
    x2=((-b)-((b**2-4*a*c)**0.5))/(2*a)
    if x1+x2==b:
        print(" the roots of the quadratic eqn are %f , %f "%(x1,x2))
    else:
        print(" the roots of the quadratic eqn are %f , %f "%(-x1,-x2))
print(" enter the a,b,c values of the quadratic eqn to be solved ",end="")
a=float(input())
b=float(input())
c=float(input())
quad(a,b,c)