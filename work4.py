import re
while True:
    try:
        A = input()
    except:
        break 
    for i in range(97,123):
        if (len(re.findall(chr(i),A)))!=0:
            print(chr(i),end=' ')
            X=(len(re.findall(chr(i),A)));
            print('*'*X,end=' ')
    for j in range(65,91):
        if (len(re.findall(chr(j),A)))!=0:
            print(chr(j),end=' ')
            X=(len(re.findall(chr(j),A)));
            print('*'*X,end=' ')