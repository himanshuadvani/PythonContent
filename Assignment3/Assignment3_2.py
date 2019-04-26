def Max(arr):
	iMax=0
	for i in range(0,len(arr)):
		if(arr[i]>iMax):
			iMax=arr[i]

	return iMax


iSize=input("Enter number of elements: ")
numbers=list()

for i in range(0,int(iSize)):
	temp=int(input("Element: "))
	numbers.append(temp)


iMax=Max(numbers)
print("Maximum number: ",iMax)
