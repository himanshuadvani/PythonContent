def Sub(no1,no2):
	return (no1-no2)

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))



def Decorator(fptr):
	def inner(no1,no2):
		if(no1<no2):
			no1,no2=no2,no1
		
		return fptr(no1,no2)
	
	return inner

Sub=Decorator(Sub)
ret=Sub(x,y)
print("Subtraction: ",ret)