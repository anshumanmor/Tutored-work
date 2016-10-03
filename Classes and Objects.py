#Classes and Objects
#Sit with end user first and figure out what the purpose of the program is
#This creates a bank account object
class BankAccount: 
	def_init_(self, name, accNo, balance):
		self.name=name 
		self.accNo=accNo
		self.balance=balance
	def deposit(self, amount):
		self.balance=self.balance+amount
	def withdraw(self, amount):
		if balance>=amount:
			self.balancee=self.balance+amount

ob1=BankAccount("Raj","127","10000")
#ob1.deposit(300)			
		
		
	


