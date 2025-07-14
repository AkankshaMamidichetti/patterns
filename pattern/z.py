rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==5 or i+j==rows+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)