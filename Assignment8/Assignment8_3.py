from threading import *;

def evenList(numbers):
	iSum=0;
	iNum=0;
	for iNum in range(0,len(numbers)):
		if(numbers[iNum]%2==0):
				iSum+=numbers[iNum]
				
	print("Even Add: ",iSum)


def oddList(numbers):
	iSum=0;
	iNum=0;
	for iNum in range(0,len(numbers)):
		if(numbers[iNum]%2==1):
				iSum+=numbers[iNum]
				
	print("Odd Add: ",iSum)

	
if __name__ == "__main__":

	numbers=[2,3,4,5,6,7,8,9,10]
	t1=Thread(target=evenList,args=(numbers,))
	t2=Thread(target=oddList,args=(numbers,))
	
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	
	print("Exit  from main")
	




	