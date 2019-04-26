def Display(num):

	for i in range(0,num):
		st=""
		for j in range(0,i+1):
			st=st+str(j+1)
		print(st)

Display(5)
