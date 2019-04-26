def chkPrime(num):
	i=2
	flag=False
	while(i<=num/2):
		if(num%i==0):
			flag=True
			break
		i=i+1

	if(flag==False):
		print("Prime Number")
	else:
		print("Not a prime number")

chkPrime(17)