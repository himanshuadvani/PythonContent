def ChkPrime(arr):
	iSum=0
	flag=0
	for i in range(0,len(arr)):
		num=2
		while(num<=arr[i]/2):
			if(arr[i]%num==0):
				flag=1
				break
			num=num+1
		if(flag==0):
			print(arr[i])
			iSum=iSum+arr[i]

	return iSum