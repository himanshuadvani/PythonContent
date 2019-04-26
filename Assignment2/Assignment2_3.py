def Fact(num):
	sum=1
	while(num>0):
		sum=sum*num
		num=num-1
	print("Factorial: ",sum)

Fact(5)