class Demo:
	Value=100;
	def __init__(self,n1,n2):
		self.no1=n1;
		self.no2=n2;

	def fun(self):
		print("First number: {0}".format(self.no1));

	def gun(self):
		print("Second number: {0}".format(self.no2));


demo=Demo(10,20);
demo.fun();
demo.gun();


demo=Demo(21,52);
demo.fun();
demo.gun();

print("Class Variable: ",Demo.Value)