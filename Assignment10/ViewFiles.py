import sys
import os


def viewfiles(path):

	if(not os.path.isabs(path)):
		path=os.path.abspath(path)

	print("Path: ",path)

	exists=os.path.isdir(path)
	for folder,subfolder,file in os.walk(path):
		print("Folder: {0}".format(folder));
		for subf in subfolder:
			print("Sub-Folder: {0}".format(subf));
		for f in file:
			if(f.endswith(sys.argv[2])):
				print("File: {0}".format(f));
				#os.rename(f,f+'.exe')
					

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