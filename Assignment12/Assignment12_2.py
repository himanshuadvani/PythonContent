import sys
import psutil;

def ProcessInfo():
	processinfo=[]
	
	for proc in psutil.process_iter():
		try:
			pinfo=proc.as_dict(attrs=['pid','name','username']);
			if(sys.argv[1].lower() in pinfo['name'].lower()):
				print(pinfo);
		
		except Exception:
			pass;
		
def main():
	print("Process Information if process is currently running...");
	print("Application Name: ",sys.argv[0])

	if(len(sys.argv)<2):
		print("invalid number of arguments...");
		exit();
		
	if(sys.argv[1]=='-h' or sys.argv[1]=='-H'):
		print("Process information if process is given process currently running...");
		exit();
	
	if(sys.argv[1]=='-u' or sys.argv[1]=='-u'):
		print("Command: python application_name process_name");
		exit();
	
	try:
		ProcessInfo();
		print()
		
	except Exception as e:
		print(e);


if __name__=="__main__":
	main();