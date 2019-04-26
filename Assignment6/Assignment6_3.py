class Arithmetic:
	
	def __init__(self):
		self.value1=0.0
		self.value2=0.0

	def Accept(self):
		self.value1=float(input("Enter first number: "));
		self.value2=float(input("Enter second number: "));

	def Addition(self):
		return self.value1+self.value2;

	def Subtraction(self):
		if(self.value1 >= self.value2):
			return self.value1-self.value2;
		else:
			return self.value2-self.value1;

	def Multiplication(self):
		return self.value1*self.value2;

	def Division(self):
		if(self.value1 >= self.value2):
			return self.value1/self.value2;
		else:
			return self.value2/self.value1;


obj1=Arithmetic();
obj1.Accept();
add1=obj1.Addition();
sub1=obj1.Subtraction();
mul1=obj1.Multiplication();
div1=obj1.Division();


print("Add: {0}, Sub: {1}, Mul: {2}, Div: {3}".format(add1,sub1,mul1,div1));

obj2=Arithmetic();
obj2.Accept();
add2=obj2.Addition();
sub2=obj2.Subtraction();
mul2=obj2.Multiplication();
div2=obj2.Division();

print("Add: {0}, Sub: {1}, Mul: {2}, Div: {3}".format(add2,sub2,mul2,div2));

