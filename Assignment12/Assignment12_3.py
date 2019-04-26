import sys
import time;
import psutil;
import os;
import re

def ProcessInfo():
	processinfo=[]
	
	dir=sys.argv[1];
	if(not os.path.exists(dir)):
		try: 
			os.mkdir(dir);
			print("Directory created...\n");
		except:
			print("Directory already exists...\n");
			pass
			
	path=os.path.join(dir,"Himanshu_Advani_%s.log"%(time.time()));
	fd=open(path,'w');
	
	seperator='-'*80;
	
	fd.write(seperator+"\n");
	fd.write("Himanshu_Advani_Process_Logger_"+(time.ctime())+"\n");
	fd.write(seperator+"\n");
	fd.write("\n");
	
	for proc in psutil.process_iter():
		try:
			pinfo=proc.as_dict(attrs=['pid','name','username']);
			pinfo['vms']=proc.memory_info().vms/(1024*1024);
			processinfo.append(pinfo);
		
		except Exception:
			pass;
			
	for element in processinfo:
		fd.write(str(element)+"\n");
		
	print("Log File created successfully...")
		
	fd.close();
		
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