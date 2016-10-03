#Write a class Bank which has a list of BankAccounts 
#A functions : Add an account , search for an account and display details, delete , deposit and withdraw
#Everything has to run on input from user
class Bank
	def_init_(self,name):
	self.name=name
	self.AccList=list()
	
	def addaccount
		name=input("Enter your account name")
		AccNo=int(input("Enter account number"))
		balance=int(input("balance"))
		Acc1= BankAccount(name,AccNo,balance)
		Acclist.append(Acc1)
		
	def displaydetail
		ans=input("Display bank account details?")
		if (ans==yes):
			print name
			print "Your account number is", AccNo
			print "Your balance is", balance
			
		
		