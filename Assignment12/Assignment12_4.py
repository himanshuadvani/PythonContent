import sys
import time;
import psutil;
import os;
import urllib.request;
import smtplib;
from email import encoders;
from email.mime.text import MIMEText;
from email.mime.multipart import MIMEMultipart;
from email.mime.base import MIMEBase;


def isconnected():
	try:
		urllib.request.urlopen('http://216.58.192.142',timeout=3);
		return True;
	except Exception as e:
		return False;
		
def MailSender(path,time):
	to=[];
	try:
		
		fromaddr="adwani708@gmail.com"
		toaddr=sys.argv[2];
		
		msg=MIMEMultipart();
		
		msg['From']=fromaddr;
		msg['To']=toaddr;
		to=toaddr.split('@');
		body="""
		Hello %s
		Please find the attached document which contains Log of Running processes.
		Log file is created at %s
		
		This is an auto generated mail. Please do not reply.
		
		Thanks and Regards,
		Himanshu Advani"""%(to[0],time);
		
		Subject="""
		Process log generated at %s
		"""%(time)
		
		msg['Subject']=Subject;

		msg.attach(MIMEText(body,'plain'));
		
		
		
		attachment=open(path,'rb');
		
		p=MIMEBase('application','octet-stream');
		
		p.set_payload((attachment).read());
		
		encoders.encode_base64(p);
		
		p.add_header('Content-Disposition',"attachment;filename=%s"%path);
		msg.attach(p);
		
		s=smtplib.SMTP('smtp.gmail.com',587);
		s.starttls();
		s.login(fromaddr,"320375Ha!");
		text=msg.as_string();
		s.sendmail(fromaddr,toaddr,text);
		s.quit();
		
		print("mail sent successfully...");
		
	except Exception as e:
		print(e);
		

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
		
	connected=isconnected();
	
	if(connected):
		print("Connected");
		startTime=time.time();
		MailSender(path,time.ctime());
		endTime=time.time();
		print("Process took %s seconds"%(endTime-startTime))
	else:
		print("No internet connection...");
	
		
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