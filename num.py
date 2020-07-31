import random
#a=5.678
#b=7.012
#c=-3.24
#print(abs(c))
#print(math.ceil(b))
#print(cmp( a,b ))
#print(math.exp(a))
#print(math.fabs(c))
#print(math.floor(a))
#print(math.log10(a))
#print(max(a,b))
#print(min(a,b))
#print(math.modf(a))
#print(pow(a,2))
#print(round(a,2))
#print(math.sqrt(b))
list=[1,2,3,4,5,6,7]
#random.seed(3)
print(random.choice(list))
print(random.randrange(1,10))
print(random.random())
random.shuffle(list)
print(list)
print(random.uniform(2,7))