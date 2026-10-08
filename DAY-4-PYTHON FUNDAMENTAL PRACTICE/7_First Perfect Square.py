l,r=map(int,input().split())
found=0
for i in range(l,r+1):
    j=0
    while j*j<i:
        j+=1
    if j*j==i:
        print("First perfect square:",i)
        found=1
        break
if not found:
    print("No perfect square found")