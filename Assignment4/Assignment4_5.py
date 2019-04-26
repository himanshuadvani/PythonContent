from functools import reduce
def MapReduce(arr):
	
	def Prime(num):
		no=2
		flag=0
		while(no<=num/2):
			if(num%no==0):
				flag=1
				break
			no=no+1

		if(flag==0):
			return True
		else:
			return False



	def chkMax(no1,no2):
		iMax=0
		if(no1>no2):
			iMax=no1
		else:
			iMax=no2

		return iMax


	filterArr=list(filter(Prime,arr))
	mapArr=list(map(lambda a:a*2,filterArr))
	result=reduce(chkMax,mapArr)
	print("MapReduce result: ",result)


iSize=input("Enter number of elements: ")
numbers=list()

for i in range(0,int(iSize)):
	temp=int(input("Element: "))
	numbers.append(temp)

MapReduce(numbers)

