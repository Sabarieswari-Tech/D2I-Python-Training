normal=large=suspicious=total=0
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        pass
    elif n<0:
        continue
    elif n<=1000:
        normal+=1
        total+=n
    elif n<=5000:
        large+=1
        total+=n
    else:
        suspicious+=1
        total+=n
        if suspicious==3:
            break
print("Normal transactions:",normal)
print("Large transactions:",large)
print("Suspicious transactions:",suspicious)
print("Total valid amount:",total)