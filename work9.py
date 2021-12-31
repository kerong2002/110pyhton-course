while(1):
    arr = list(map(int,input().split()))
    if(arr[0]>0):
        sum1=0
        sum0=0
        N=arr[0]
        arr.remove(N)
        arr.sort()
        if(N%2==0):
            s=int(N/2-1)
        else:
            s=int(((N+1)/2)-1)
        u = sum(arr)/N
        for i in arr:
            sum1 += (i-u)**2 
        print(arr[s],int(sum1/N))
    else:
        break