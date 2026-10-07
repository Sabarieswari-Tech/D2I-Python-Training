x=int(input())
if x<0:
    print(False)
else:
    temp=x
    rev=0
    while temp>0:
        rev=rev*10+temp%10
        temp//=10
    print(x==rev)