a=int(input("Enter the age"))
if a<18:
	print("\t\nNot eligible to vote")
elif a>=18 and a<60:
	print("\t\nEligible to vote")
elif a>=60:
	print("\nsenior citizen")
else:
	print("\nchild")