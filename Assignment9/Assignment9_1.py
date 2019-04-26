
filename=input("Enter file name: ");
fd=None;

try:
	fd=open(filename,'r',encoding = 'utf-8')

except Exception: 
	print("File Not found...")

finally:
	if(fd!=None):
		print("File found...");
		
	fd.close();

	