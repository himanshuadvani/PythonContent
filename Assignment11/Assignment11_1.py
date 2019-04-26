import os
import sys
import hashlib

def FileHash(path):
	hash=hashlib.md5()
	block=1024;
	fd=open(path,'rb');
	data=fd.read(block);
	while(len(data)>0):
		hash.update(data);
		data=fd.read(block)
		
	fd.close();
	return hash.hexdigest()
		
	

def AllFiles(path):
	path=os.path.abspath(path);
	exists=os.path.isdir(path);
	
	if(exists):
		for folder,subfolders,files in os.walk(path):
			print("\nFolder: ",folder);
			
			for i in subfolders:
				print("Subfolder: ",i);
	
			for j in files:
				print("File: ",j);
				hash=FileHash(os.path.join(folder,j));
				print("Hashcode: ",hash,"\n");
				
	

def main():
	print("\nAutomation for checksum....");
	print("Application name: {0}".format(sys.argv[0]));
	
	if( (sys.argv[1]=='-h') or  (sys.argv[1]=='-H') ):
		print("\nHelp\nAutomation script to display checksum of all files");
		exit();
	
	if( (sys.argv[1]=='-u') or  (sys.argv[1]=='-U') ):
		print("\nUsage\nExecute: python application_name options");
		exit();
		
	try:
		AllFiles(sys.argv[1])
	
	except Exception as e:
		print(e);
	

if __name__=="__main__":
	main()