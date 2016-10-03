#Any live cell with fewer than two live neighbors dies
#Any live cell with two or three live neighbors lives
#Any live cell with more than 3 live neighbours dies
#Any dead cell with exactly 3 live neighbors becomes alive
def matrix()
	row1=[1,0,1,0,0]
	row2=[0,1,0,1,1]
	row3=[0,1,1,1,0]
	row4=[1,0,1,0,1]
	row5=[0,1,1,0,1]
	matrix=[row1,row2,row3,row4,row5]
	
def deadcellrule()
	a=0
	b=0
	count=0
	while ():
	if(matrix[a][b]==0):
		if a!=0 and b!=0 and matrix[a-1][b-1]==1
			count=count+1
		if a!=0 and matrix[a-1][b]==1
			count=count+1
		if a!=0 and matrix[a-1][b+1]==1  
			count=count+1
		if matrix[b]!=0 and matrix[a][b-1]==1
			count=count+1
		if matrix[a][b+1]==1
			count=count+1
		if matrix[a+1][b-1]==1
			count=count+1
		if matrix[a+1][b]==1
			count=count+1
		if matrix[a+1][b+1]==1
			count=count+1
		if count==3
			matrix[a][b]=1
	
def alive1():

def alive2():

def alive3():

def 
			
	
