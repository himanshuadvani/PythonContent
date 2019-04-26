from threading import *;



def Display():
	i=0
	for i in range(1,51):
		print(i)


def Reverse():
	i=50
	while(i>0):
		print(i)
		i=i-1

			
				
if __name__ == "__main__":

	
	t1=Thread(target=Display,args=())
	t2=Thread(target=Reverse,args=())
	
	t1.start()
	t1.join()
	
	t2.start()
	t2.join()

	
	print("Exit  from main")
	

