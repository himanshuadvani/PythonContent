import sys;
import requests;
import os;
from urllib.parse import urlparse

def isDownloadable(url):
	h=requests.head(url,allow_redirects=True);
	header=h.headers;
	content_type=header.get('content-type');
	print(content_type);
	
	if('text' in content_type.lower()):
		return False;
		
	if('html' in content_type.lower()):
		return False;
		
	return True

def getfilename(url):
	temp=urlparse(url)
	return os.path.basename(temp.path)


def fileDownload(url):
	allowed=isDownloadable(url);
	
	if allowed:
		try:
			res=requests.head(url,allow_redirects=True,verify=False)
			filename=getfilename(url);
			fd=open(filename,'wb');
			
			for buff in res.iter_content(1024):
				fd.write(buff)
				
			fd.close();	
			return True;
		
		except Exception as e:
			print(e);
			return False;
			
	else:
		return False;

def main():
	print("Automation scipt to download a file from the given url...");
	print("Application Name: ",sys.argv[0]);
	
	url="https://leusea-34318.firebaseapp.com/programming-in-c-3-e-a-practical-approach-by-ajay-mittal.pdf"
	result=fileDownload(url);
	if(result==True):
		print("File downloaded successfully...");
	else:
		print("Failed to download...");
		
	

if __name__=="__main__":
	main()