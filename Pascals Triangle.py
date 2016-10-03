def factorial(num):
	div=1
	product=num
	if(num==0):
		return 1
	while(div<num):	
		fact=num-div
		div=div+1
		product=product*fact
	return product

def triangle():
n=0
while(n<5):
	r=0
	while(r<=n):
		ans=factorial(n)/(factorial(r)*(factorial(n-r))
		print ans
		r=r+1
	n=n+1
	print "\n"
			
		
		
		
		
	
	
