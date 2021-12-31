a=input()
for i in range(0,int(a)):
    line = input()
    A,B,C= line.split()
    A,B,C= int(A),str(B),str(C)
    for x in range (1,A+1):
        print(B*x,end='')
        for y in range(A-x):
	        print(C,end='')
        print()