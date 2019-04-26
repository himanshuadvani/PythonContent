class Arithmetic:

	def __init__(self,num):
		self.value=num;

	def CheckPrime(self):
		i=2;
		while(i<=self.value/2):
			if(self.value%i==0):
				break;
			i=i+1;

		if(i>self.value/2):
			return True;
		else:
			return False;


	def CheckPerfect(self):
		i=1;
		sum=0;
		while(i<=self.value/2):
			if(self.value%i==0):
				sum=sum+i
			i=i+1

		if(sum==self.value):
			return True;
		else:
			return False;

	def Factors(self):
		i=1;
		fact=list();
		while(i<self.value):
			if(self.value%i==0):
				fact.append(i);
			i=i+1;

		print(fact);


	def SumFactors(self):
		i=1;
		sum=0;
		fact=list();
		while(i<self.value):
			if(self.value%i==0):
				sum=sum+i
			i=i+1;

		return sum;

obj=Arithmetic(6);
print("Number: ",obj.value);
print("Prime: ",obj.CheckPrime())
print("Perfect: ",obj.CheckPerfect())
print("Factors: ",obj.Factors())
print("Sum of Factors: ",obj.SumFactors())