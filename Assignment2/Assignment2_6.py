def Display(num):
	star="*"
	i=num
	while(i>0):
		str=""
		j=0
		while(j<i):
			str=str+star
			j=j+1
		print(str)
		i=i-1

Display(5)