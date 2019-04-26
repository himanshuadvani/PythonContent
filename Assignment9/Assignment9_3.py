from sys import *;

newFile=input("Enter new file name: ");
fd1=None;
fd2=None;
data=None;

try:
	fd1=open(argv[1],'r',encoding='utf-8');
	data=fd1.read();
	fd2=open(newFile,'a',encoding='utf-8');
	fd2.write(data);
	
except:
	print("File not found...");
	
finally:
	fd1.close();
	fd2.close();