def sumDigits(num):
	sum=0
	while(num!=0):
		sum=sum+int(num%10)
		num=num/10
	return sum

result=sumDigits(5187)
print("Sum of digist: ",result)