list=[-3, 14, -7, -11, 12]
count=5
while(count>1):
	maxPos=0
	pos=1
	while(pos<count):
		if(list[pos]>list[maxPos]):
			maxPos=pos
		pos=pos+1
	temp=list[maxPos]
	list[maxPos]=list[count-1]
	list[count-1]=temp
	count=count-1
print list