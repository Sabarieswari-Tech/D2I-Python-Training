n=int(input())
skipped=0
for i in range(1,21):
    x=n*i
    if x>100:
        break
    if x%3==0:
        skipped+=1
        continue
    print(n,"x",i,"=",x)
print("Skipped results:",skipped)