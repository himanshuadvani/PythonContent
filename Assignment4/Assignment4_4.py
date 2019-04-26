from functools import reduce
def MapReduce(arr):

	filterArr=list(filter(lambda a:a%2==0,arr))
	mapArr=list(map(lambda a:a*a,filterArr))
	result=reduce(lambda a,b:a+b,mapArr)
	print("Map reduce: ",result)	


iSize=input("Enter number of elements: ")
numbers=list()

for i in range(0,int(iSize)):
	temp=int(input("Element: "))
	numbers.append(temp)

MapReduce(numbers)

