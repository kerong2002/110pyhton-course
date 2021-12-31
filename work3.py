while True:
    try:
        line = input()
    except:
        break 
    A,B,C= line.split()
    A,B,C= int(A),int(B),int(C)
    if A ==1:
        print(1,end=' ')
        if B > C :
            X= B
        else:
            X = C
        for k in range(2, X): 
            if B % k == 0 and B % k == 0:
                if k<100:
                    print(k,end=' ')
        print()
                       
    if A==2:
        if B > C :
            Y = B
        else:
            Y = C
        m = (B + 1) * (C + 1)
        for g in range(Y, m):
            if g % B == 0 and g % C == 0:
                if (g>=100):
                    print("None")
                    break
                if g<100:
                    for i in range(1,100):
                        if (g*i<100):
                            print(g*i,end=' ')
                    print()
                break  