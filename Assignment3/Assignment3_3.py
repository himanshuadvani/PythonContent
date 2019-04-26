def Min(arr):
	iMin=arr[0]
	for i in range(1,len(arr)):
		if(arr[i]<iMin):
			iMin=arr[i]

	return iMin


iSize=input("Enter number of elements: ")
numbers=list()

for i in range(0,int(iSize)):
	temp=int(input("Element: "))
	numbers.append(temp)


iMin=Min(numbers)
print("Minimum number: ",iMin)
