//This program prints all perfect numbers using two functions
def isPerfect(num):
	sum=0
	div=0
	while(div<num):
		if(num%div==0):
			sum=sum+div
		div=div+1
	if(sum==num):
		return 1
	else:
		return 0
def perfectsInList():
	list=[1,7,9,28,6,32]
	pos=0
	while(pos<6):
		ans=isPerfect(list[pos])
		if(ans==1):
			print list[pos]
		pos=pos+1