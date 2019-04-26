from threading import *;

def Small(source):
	i=0
	for i in range(0,len(source)):
		if(ord(source[i])>=97 and ord(source[i])<=122):
			print("Small character: ",source[i]);


def Capital(source):
	i=0
	for i in range(0,len(source)):
		if(ord(source[i])>=65 and ord(source[i])<=90):
			print("Capital character: ",source[i]);
			


def Digits(source):
	i=0
	for i in range(0,len(source)):
		if(ord(source[i])>=48 and ord(source[i])<=57):
			print("Digit: ",source[i]);
			
			
				
if __name__ == "__main__":

	numbers=[2,3,4,5,6,7,8,9,10]
	t1=Thread(target=Small,args=("HIMAnshu1234",))
	t2=Thread(target=Capital,args=("HIMAnshu1234",))
	t3=Thread(target=Digits,args=("HIMAnshu1234",))
	
	
	t1.start()
	t2.start()
	t3.start()
	
	t1.join()
	t2.join()
	t3.join()
	
	print("Exit  from main")
	

