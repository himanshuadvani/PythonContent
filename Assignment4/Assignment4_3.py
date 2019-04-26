from functools import reduce
def MapReduce(arr):

	def chkNum(num):
		return (num>=70 and num<=90)

	filterArr=list(filter(chkNum,arr))
	mapArr=list(map(lambda num:num+10,filterArr))
	result=reduce(lambda a,b:a*b,mapArr)
	print("After Filter, Map and Reduce operation: Result is ",result)

iSize=input("Enter number of elements: ")
numbers=list()

for i in range(0,int(iSize)):
	temp=int(input("Element: "))
	numbers.append(temp)

MapReduce(numbers)

