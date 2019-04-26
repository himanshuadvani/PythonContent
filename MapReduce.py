from functools import reduce
arr=[1,2,3,4,5,8,7,63]



#Filter
def divByTen(no):
	if (no%2==0):
		return True
	else:
		return False

divArr=list(filter(lambda no:no%2==0,arr))
print("After Filter: ",divArr)


#Map 
def fact(no):
	iMul=1 
	while(no!=0):
		iMul=iMul*no
		no=no-1

	return iMul

factArr=list(map(fact,divArr))
print("After Map: ",factArr)


#Reduce
#def add(a,b):
#	return a+b

sum=reduce(lambda a,b:a+b,factArr)
print("After Reduce: ",sum)