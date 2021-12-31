def adddocument():
    test=1
    for x in range(len(data)):
        if(active[1]==data[x][0]):
            print("Exist")
            test=2
    if(test==1):
        data.append(active[1:5])
    # print(data)
def deletedocument():
    test=1
    for x in range(len(data)-1,-1,-1):
        if(active[1]==data[x][0]):
            data.remove(data[x][0:4])
            test=2
    if(test==1):
        print("None")    
    # print(data)
    # print("document delete")
def changedocument():
    test=1
    act=int(active[2])
    for x in range(len(data)):
        if(active[1]==data[x][0]):
            if(act==0):  
                data[x][1]=active[3]
            if(act==1): 
                data[x][2]=active[3]
            if(act==2):  
                data[x][3]=active[3]
            test=2
    if(test==1):
        print("None")    
    # print("document change")
def viewdocument():
    test=1
    act=int(active[2])
    for x in range(len(data)):
        if(active[1]==data[x][0]):
            if(act==0):  
                print(data[x][1])
            if(act==1): 
                print(data[x][2])
            if(act==2):  
                print(data[x][3])
            test=2
    # print(active[2])  
    # print(data[1][1])
    if(test==1):
        print("None")
data=[]
while True:
    active = input()
    active = active.split()
    if(active[0]=="*"):
        break
    else:   
        if(active[0]=='@'):
            adddocument()
        if(active[0]=='#'):
            deletedocument()
        if(active[0]=='!'):
            changedocument()
        if(active[0]=='$'):
            # print(data)
            viewdocument()

#@ 1 kerongchen  0976351920 1118 
#@ 2 yayun 0933245535 0131 
#@ 3 yuyun 097624575 0424