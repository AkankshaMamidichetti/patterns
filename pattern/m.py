rows=5
mid=(rows//2)+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i<=mid:
            if j==1 or j==rows or i==j or i+j==rows+1:
                res+="*"+" "
            else:
                res+=" "+" "
        else:
            if j==1 or j==rows:
                res+="*"+" "
            else:
                res+=" "+" "
    print(res)