def asciiSum(s):
	iSum=0
	iAvg=0
	for i in range(0,len(s)):
		iSum=iSum+ord(s[i])
	iAvg=iSum/len(s)

	return iAvg




def deleteChar(s,pos):
	if(pos-1>len(s)):
		print("Please enter correct position...")
		return
	s=s[:pos-1]+s[pos:]
	print("Final String: ",s)
	print(len(s))	


def wordCount(s):
	iCount=1
	i=0
	if(s[0]==" "):
		iCount=0

	while(i<len(s)):	
		if(s[i]==" "):
			iCount=iCount+1
			while(s[i]==" "):
				if(i==(len(s)-1)):
					return iCount-1	
				i=i+1
		i=i+1	
	return iCount


def strRev(s):
	i=0
	j=(len(s)-1)

	res=""
	

	while(i<=(len(s)-1) and j>=0):
		res=res[:i]+s[j]+res[i+1:]
		j=j-1
		i=i+1
		

	return res