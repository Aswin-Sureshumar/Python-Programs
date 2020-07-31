import sys
try:
    a=int(input(" Enter a value : "))
    print(a.isalpha())
except:
	if a==0:
		print("Zero")
else:
	if a==10:
		print("F")
finally:
	print("End") 

