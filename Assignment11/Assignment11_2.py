import sys
import os
import hashlib


def filehash(filepath):
	hash=hashlib.md5();
	block=1024;
	fd=open(filepath,'rb');
	buffer=fd.read(block)
	
	while(len(buffer)>0):
		hash.update(buffer)
		buffer=fd.read(block)
		
	fd.close()
	
	return hash.hexdigest()


def AllFiles(path):
	path=os.path.abspath(path)
	exists=os.path.isdir(path);
	
	dict={};
	
	if(exists):
		for folder,subfolder,file in os.walk(path):
			for i in file:
				filepath=os.path.join(folder,i);
				hash=filehash(filepath);
				
				if hash in dict:
					dict[hash].append(filepath)
				else:
					dict[hash]=[filepath]
					
	
	
		
	else:
		print("Invalid path...");
		
	return dict;
	
	
def PrintFiles(dict):
	count=0;
	arr=list(filter(lambda x:len(x)>1,dict.values()));
	print("\nDuplicate Files...");
	for i in arr:
		for j in i:
			print("\n",j);
		


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
		arr=AllFiles(sys.argv[1]);
		PrintFiles(arr);
	
	except Exception as e:
		print(e);
	
	

if __name__=="__main__":
	main()