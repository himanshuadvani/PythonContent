import sys
import os
import hashlib
import time


def printduplicate(dict):
	arr=list(filter(lambda x:len(x)>1,dict.values()));
	print("\nDuplicate Files...");
	for i in arr:
		for j in i:
			print("\n",j);
			
	return arr;
	
def deleteduplicate(files):
	count=0;
	for i in files:
		for j in i:
			count+=1
			if(count>=2):
				print("\nDeleting file: ",j,"....");
				os.remove(j)
	
		count=0;
			

	


def filehash(filepath):
	block=1024;
	fd=open(filepath,'rb');
	hash=hashlib.md5();
	data=fd.read(block)
	
	while(len(data)>0):
		hash.update(data);
		data=fd.read(block);
		
	fd.close()
	
	return hash.hexdigest()
	
	


def AllFiles(path):
	path=os.path.abspath(path);
	exists=os.path.isdir(path);
	
	dict={};
	
	if exists:
		for folder,subfolder,file in os.walk(path):
			for i in file:
				filepath=os.path.join(folder,i);
				hash=filehash(filepath);
				
				if hash in dict:
					dict[hash].append(filepath)
				else:
					dict[hash]=[filepath];
				
	else:
		print("invalid path...");

	return dict;


def main():
	arr={};
	print("\nAutomation for finding duplicate files....");
	print("Application name: {0}".format(sys.argv[0]));
	
	if( (sys.argv[1]=='-h') or  (sys.argv[1]=='-H') ):
		print("\nHelp\nAutomation script to display duplicate files");
		exit();
	
	if( (sys.argv[1]=='-u') or  (sys.argv[1]=='-U') ):
		print("\nUsage\nExecute: python application_name options");
		exit();
		
	try:
		start=time.time();
		arr=AllFiles(sys.argv[1]);
		files=printduplicate(arr)
		deleteduplicate(files)
		end=time.time();
		print("time taken: ",end-start);
	
	except Exception as e:
		print(e);
	

if __name__=="__main__":
	main()