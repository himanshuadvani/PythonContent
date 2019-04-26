def AddFactors(num):
	i=1
	sum=0
	while(i<=num/2):
		if(num%i==0):
			sum=sum+i
		i=i+1
	print("Addition of factors: ",sum)


AddFactors(15)
