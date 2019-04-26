import psutil;

def ProcessDisplay():
	processes=[];
	
	for proc in psutil.process_iter():
		try:
			temp=proc.as_dict(attrs=['pid','name','username']);
			temp['vms']=proc.memory_info().vms;
			processes.append(temp);
		except Exception as e:
			pass
			
	return processes;

def main():
	print("Process monitor with memory usage...");
	processes=ProcessDisplay();
	
	for value in processes:
		print(value);


if __name__=="__main__":
	main()
	