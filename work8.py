while True:
    try:
        line = input()
    except:
        break 
    N,B = line.split()
    N,B = int(N),int(B)
    
    def covert(N ,B):
        convertstring="0123456789"
        if N < B:
            return convertstring[N]
        else:
            return covert(N//B,B) + convertstring[N%B]
        
    if(N>0 and(B>1 and B<=10)):
        result = covert(N,B)
        print(result)

    else:
        break