def Display(num):
	i=num
	star="*"
	
	while(i>0):
		j=num
		str=""	
		while(j>0):
			str=str+star
			j=j-1
		print(str)
		i=i-1

num=int(input("Enter number: "))
Display(num)