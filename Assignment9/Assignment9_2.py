
filename=input("Enter file name: ");
fd=None;
data=None;

try:
	fd=open(filename,'r',encoding='utf-8');
	data=fd.read();
	print("Data from file: ",data);
	
except Exception:
	print("File not found...");
	
finally:
	
	fd.close();



