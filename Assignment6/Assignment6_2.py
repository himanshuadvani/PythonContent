class Circle:
	PI=3.14

	def __init__(self):
		self.Radius=0.0;
		self.Area=0.0;
		self.Circum=0.0;

	def Accept(self):
		self.Radius=float(input("Enter Radius: "));


	def CalculateArea(self):
		self.Area=Circle.PI*self.Radius*self.Radius;
		return self.Area;

	def CalculateCircum(self):
		self.Circum=2*Circle.PI*self.Radius;
		return self.Circum;

obj=Circle();
obj.Accept();
area=obj.CalculateArea();
circum=obj.CalculateCircum();

obj2=Circle();
obj2.Accept();
area2=obj2.CalculateArea();
circum2=obj2.CalculateCircum();


print("Circumference: {0} and Area: {1}".format(circum,area));

print("Circumference: {0} and Area: {1}".format(circum2,area2));
