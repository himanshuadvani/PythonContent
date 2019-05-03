import requests;
import bs4;
import urllib.request;
import webbrowser;
import sys;
from urllib.parse import urlparse;
import os;


def isconnected():
	try:
		urllib.request.urlopen('http://216.58.192.142',timeout=3);
		return True;
	except Exception as e:
		print(e);
		return False;
		
		
		
def isDownloadable(url):
	h=requests.head(url,allow_redirects=True,verify=False);
	header=h.headers;
	content_type=header.get('content-type');
	print(content_type);
	
	if('text' in content_type.lower()):
		return False;
		
	if('html' in content_type.lower()):
		return False;
		
	return True;
	

def getfilename(url):
	temp=urlparse(url)
	return os.path.basename(temp.path)


def fileDownload(url):
	allowed=isDownloadable(url);
	
	if allowed:
		try:
			res=requests.get(url,allow_redirects=True,verify=False)
			filename=getfilename(url);
			fd=open(filename,"wb");
			
			for buff in res.iter_content(1024):
				fd.write(buff)
				
			fd.close();	
			buff=None;
			return True;
		
		except Exception as e:
			print(e);
			return False;
			
	else:
		return False;
		
def getImages(url):
	conn=urllib.request.urlopen(url);


	res=conn.read();
	conn.close()
	data=bs4.BeautifulSoup(res,'html.parser');

	images=data.findAll("img");

	
		
	return images;


def main():
	images=[];
	print("Automation scipt to download a file from the given url...");
	print("Application Name: ",sys.argv[0]);
	
	url="https://www.amazon.in/s?k=dell+laptops&crid=O2DEVBZI6OF7&sprefix=dell+laptop%2Caps%2C311&ref=nb_sb_ss_i_1_11"
	images=getImages(url)
	print("Length: ",len(images),"\n");
	
	count=1;

	for i in images:
		
		print("Count: ",count);
		count+=1;
		print(i['src']);
		result=fileDownload(i['src']);
		if(result==True):
			print("File downloaded successfully...");
		else:
			print("Failed to download...");
		
		print("\n");
	
		
	

if __name__=="__main__":
	main()