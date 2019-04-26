from sys import *;

file1=argv[1];
file2=argv[2];
fd1=None;
fd2=None;
data1=None;
data2=None;

try:
	fd1=open(file1,'r',encoding='utf-8');
	data1=fd1.read();
	
	fd2=open(file2,'r',encoding='utf-8');
	data2=fd2.read();
	
	if(data1==data2):
		print("SUCCCESS");
	else:
		print("FAILURE");
except:
	print("File not found...");

finally:
	fd1.close();
	fd2.close();