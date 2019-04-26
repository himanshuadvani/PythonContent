def Frequency(arr,no):
	iCount=0
	for i in range(len(arr)):
		if(arr[i]==no):
			iCount=iCount+1

	return iCount

iSize=input("Enter number of elements: ")
numbers=list()

for i in range(0,int(iSize)):
	temp=int(input("Element: "))
	numbers.append(temp)

num=int(input("element element to be searched: "))

ret=Frequency(numbers,num)
print("Frequency of {0} is {1}".format(num,ret))