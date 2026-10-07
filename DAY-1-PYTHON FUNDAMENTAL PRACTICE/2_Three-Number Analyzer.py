a,b,c=map(int,input().split())
n=int(input())
print("Largest:",max(a,b,c))
print("Smallest:",min(a,b,c))
print(f"Average: {(a+b+c)/3:.2f}")
if n>0:
    if n%2==0:
        print("Classification: Positive and Even")
    else:
        print("Classification: Positive and Odd")
elif n<0:
    if n%2==0:
        print("Classification: Negative and Even")
    else:
        print("Classification: Negative and Odd")
else:
    print("Classification: Zero")