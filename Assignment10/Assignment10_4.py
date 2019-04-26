import sys
import os
import shutil


def viewfiles(path):

	if(not os.path.isabs(path)):
		path1=os.path.abspath(path)
		
	path2=os.path.abspath(sys.argv[2])
	exists1=os.path.isdir(path1)
	exists2=os.path.isdir(path2)
	if(exists1):
		for folder,subfolder,file in os.walk(path1):
			for f in file:
				if(f.endswith(sys.argv[3])):
					shutil.copy(os.path.join(folder,f),path2)
					
					
	print("All files copied...");

def main():
	print("Application Name: ",sys.argv[0]);

	if(len(sys.argv)<2 or len(sys.argv)>5):
		print("Error: Invalid number fo arguments.");

	if(sys.argv[1]=="-h" or sys.argv[1]=="-H"):
		print("This appication is used to view file names with specific extension.");
		exit();

	if(sys.argv[1]=="-u" or sys.argv[1]=="-U"):
		print("Execution: python file_name .extension(eg: .exe,.pdf,etc.)");
		exit()

	try:
		viewfiles(sys.argv[1])

	except Exception as e:
		print(e); 


if __name__=="__main__":
	main()