import MarvellousNum as mn

iSize=input("Enter number of elements: ")
numbers=list()

for i in range(0,int(iSize)):
	temp=int(input("Element: "))
	numbers.append(temp)

ret=mn.ChkPrime(numbers)
print("Addition of prime numbers: ",ret)