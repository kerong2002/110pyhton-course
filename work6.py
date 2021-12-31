A_win_combination = [["M", "Y"], ["O","M"], ["Y","O"]]
B_win_combination = [["Y", "M"], ["M","O"], ["O","Y"]]

while True:
    try:
        k=int(input())
        count=k
        x=0
        y=0
    except:
        break
    if(k%2==1):
        while(count>0):
            s =""
            s = list(map(str,input().split()))
            if s in A_win_combination:
                x=x+1
                count=count-1
                if(x==((k+1)/2)):
                    print ("The first person wins the game")
                    break
            elif s in B_win_combination:
                y=y+1
                count=count-1
                if(y==((k+1)/2)):
                    print ("The second person wins the game")
                    break
    elif(k%2==0):
        break