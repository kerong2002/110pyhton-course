A=""
B=""
C=""
for i in range(1,10): 
     for j in range(1,10):
        if (i % 2 )!= 0:
            A=A+"{} X {} = {}".format(i,j,i*j)+'\n'
        if(i % 2)==0 and (j % 2)!=0:
            B=B+"{} X {} = {}".format(i,j,i*j)+'\n'
        if(i % 2)==0 and (j % 2)==0:
            C=C+"{} X {} = {}".format(i,j,i*j)+'\n'
print(A)
print(B)
print(C)