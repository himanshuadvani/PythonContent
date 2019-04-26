class BankAccount:
	ROI=10.5;

	def __init__(self,name,amt):
		self.Name=name;
		self.Amount=amt;

	def Display(self):
		print("Name: {0},Amount: {1}".format(self.Name,self.Amount));

	def Deposit(self,amt):
		self.Amount+=amt;
		print("Deposit: ",self.Amount);

	def Withdraw(self,amt):
		self.Amount-=amt;
		print("Withdraw: ",self.Amount);

	def CalculateInterest(self):
		print("Interest: ",(self.Amount*BankAccount.ROI)/100);


name=input("Enter name: ");
amt=float(input("Enter amount: "));
obj1=BankAccount(name,amt);

obj1.Deposit(100);
obj1.Withdraw(50);
obj1.CalculateInterest();
obj1.Display();