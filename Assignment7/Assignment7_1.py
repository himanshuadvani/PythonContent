class BookStore:
	NoOfBooks=0;

	def __init__(self,name,auth):
		self.Name=name;
		self.Author=auth;
		BookStore.NoOfBooks+=1;

	def Display(self):
		print("Name: {0}, Author: {1}, No of Books: {2}".format(self.Name,self.Author,BookStore.NoOfBooks))

obj1=BookStore("Linux System Programming","Robert Love");
obj1.Display();

obj2=BookStore("C Programming","Ajay Mittal");
obj2.Display();
