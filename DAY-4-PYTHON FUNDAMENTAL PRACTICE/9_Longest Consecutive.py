n=int(input())
a=list(map(int,input().strip()))
cur=a[0]
count=1
best=a[0]
bestcount=1
for i in range(1,n):
    if a[i]==cur:
        count+=1
    else:
        cur=a[i]
        count=1
    if count>bestcount:
        bestcount=count
        best=cur
print("Value =",best)
print("Length =",bestcount)