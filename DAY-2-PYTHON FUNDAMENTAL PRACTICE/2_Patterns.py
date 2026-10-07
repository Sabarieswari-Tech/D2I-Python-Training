n=int(input())
print("Right Triangle")
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()
print("Pyramid")
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
print("Number Triangle")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
print("Multiplication Grid")
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}",end="  ")
    print()