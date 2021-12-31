while True:
    try:
        line = input()
    except:
        break 
    A,B = line.split()
    A,B = int(A),int(B)
    if A == B:
        print('A tie')
    elif A ==2 and B==1 :
        print('The first man wins the game')
    elif A ==3 and B==2 :
        print('The first man wins the game')
    elif A ==1 and B==3 :
        print('The first man wins the game')
    else:
        print('The second man wins the game')  
# win_combination = [["2", "1"], ["3","2"], ["1","3"]]

# while True:
#     try:
#         line = input()
#     except:
#         break
#     A,B = line.split()
#     if A == B:
#         print ("A tie")
#     elif [A, B] in win_combination:
#         print ("The first man wins the game")
#     else:
#         print ("The second man wins the game")