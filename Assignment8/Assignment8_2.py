from threading import *;

def evenFactor(number):
	iSum=0;
	iNum=0;
	for iNum in range(1,number):
		if(number%iNum==0):
			if(iNum%2==0):
				iSum+=iNum
				
	print("Even Add: ",iSum)


def oddFactor(number):
	iSum=0;
	iNum=0;
	for iNum in range(1,number):
		if(number%iNum==0):
			if(iNum%2==1):
				iSum+=iNum
				
	print("Odd Add: ",iSum)
	
	
if __name__ == "__main__":
	t1=Thread(target=evenFactor,args=(18,))
	t2=Thread(target=oddFactor,args=(18,))
	
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	
	print("Exit  from main")
	




	