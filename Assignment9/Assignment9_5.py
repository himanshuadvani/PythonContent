from sys import *;

file=argv[1];
word=argv[2];
fd=None;
data=None;
count=0

try:
	fd=open(file,'r',encoding='utf-8');
	data=fd.read();
	data=data.split();
	for i in range(0,len(data)):
		if(word==data[i]):
			count+=1;
			
	print("frequency of {0} is {1}".format(word,count));
	
except:	
	print("File not found...");
	
finally:
	fd.close();
