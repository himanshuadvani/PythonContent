def Summation(arr):
	iSum=0
	for i in range(0,len(arr)):
		iSum=iSum+arr[i]

	return iSum


iSize=int(input("Enter number of elements: "))
numbers=list()


for i in range(0,iSize):
	temp=input("Element: ")
	numbers.append(int(temp))

ret=Summation(numbers)
print("Sum of {0} is {1}".format(numbers,ret))
