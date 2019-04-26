import sys
import schedule
import os
import hashlib
import time
import urllib.request;
import smtplib;
from email import encoders;
from email.mime.text import MIMEText;
from email.mime.multipart import MIMEMultipart;
from email.mime.base import MIMEBase;


def writeToLog(deletedFiles):
	dir="Output"
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
	
	filecount=len(deletedFiles);
	
	for element in deletedFiles:
		fd.write(str(element)+"\n");
		
	return filecount,path;

def isconnected():
	try:
		urllib.request.urlopen('http://216.58.192.142',timeout=3);
		return True;
	except Exception as e:
		return False;
		
def MailSender(path,fileCount,allCount,start,end):
	to=[];
	try:
		
		fromaddr="adwani708@gmail.com"
		toaddr=sys.argv[3];
		
		msg=MIMEMultipart();
		
		msg['From']=fromaddr;
		msg['To']=toaddr;
		to=toaddr.split('@');
		body="""
		Hello %s
		Please find the attached document which contains Log of Duplicate Deleted files.
		Start time of scanning: %s
		Total files scanned: %s
		Total duplicate files deleted: %s
		
		This is an auto generated mail. Please do not reply.
		
		Thanks and Regards,
		Himanshu Advani"""%(to[0],start,allCount,fileCount);
		
		Subject="""
		Log of duplicate file deletion generated at %s
		"""%(time.ctime());
		
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





def printduplicate(dict):
	arr=list(filter(lambda x:len(x)>1,dict.values()));
	print("\nDuplicate Files...");
	for i in arr:
		for j in i:
			print("\n",j);
			
	return arr;
	
def deleteduplicate(files):
	count=0;
	deletedFiles=[];
	for i in files:
		for j in i:
			count+=1
			if(count>=2):
				print("\nDeleting file: ",j,"....");
				deletedFiles.append(j);
				os.remove(j)
	
		count=0;
		
	return deletedFiles;
			

	


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
	allCount=0;
	dict={};
	
	if exists:
		for folder,subfolder,file in os.walk(path):
			for i in file:
				allCount+=1;
				filepath=os.path.join(folder,i);
				hash=filehash(filepath);
				
				if hash in dict:
					dict[hash].append(filepath)
				else:
					dict[hash]=[filepath];
					
				
				
	else:
		print("invalid path...");

	return dict,allCount;

def fun_Minute():
	try:
		start=time.time();
		arr,allCount=AllFiles(sys.argv[1]);
		files=printduplicate(arr)
		deletedFiles=deleteduplicate(files);
		print("Deleted Files are: ",deletedFiles);
		fileCount,path=writeToLog(deletedFiles);
		end=time.time();
		print("Time taken: ",end-start);
		
		connected=isconnected();
	
		if(connected):
			print("Connected");
			MailSender(path,fileCount,allCount,start,end);
			print("Process took %s seconds"%(end-start))
		else:
			print("No internet connection...");
	
	except Exception as e:
		print(e);
	
def main():
	deletedFiles=[];
	arr={};
	print("\nAutomation for finding duplicate files and sending log of duplicate files through email....");
	print("Application name: {0}".format(sys.argv[0]));
	
	if( (sys.argv[1]=='-h') or  (sys.argv[1]=='-H') ):
		print("\nHelp\nAutomation script to display duplicate files and send log of duplicate files through email.");
		exit();
	
	if( (sys.argv[1]=='-u') or  (sys.argv[1]=='-U') ):
		print("\nUsage\nExecute: python application_name options");
		exit();
		
	try:
		schedule.every(int(sys.argv[2])).minutes.do(fun_Minute);
		
		while(True):
			schedule.run_pending();
	
	except Exception as e:
		print(e);
	

if __name__=="__main__":
	main()