from threading import *; 

def Even():
    iNum=0
    iCount=0
    while(iCount<10):
        if(iNum%2==0):
            print("Even Number {0}: {1}".format(iCount+1,iNum))
            iCount+=1
        iNum+=1
		
def Odd():
    iNum=0
    iCount=0
    while(iCount<10):
        if(iNum%2==1):
            print("Odd Number {0}: {1}".format(iCount+1,iNum))
            iCount+=1
        iNum+=1
		
if __name__ == "__main__":

	t1=Thread(target=Even,args=())
	t2=Thread(target=Odd,args=())

	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	
	print("End of thread execution,back to process...")

        
