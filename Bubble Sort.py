list=[5,2, -36, 29, 1, 12, -14]
count=7
while(count>1):
	pos=0	
	while(pos<count-1):
		if(list[pos]>list[pos+1]):
			temp=list[pos+1]
			list[pos+1]=list[pos]
			list[pos]=temp
		pos=pos+1 
	count=count-1
print list
	
	
	
