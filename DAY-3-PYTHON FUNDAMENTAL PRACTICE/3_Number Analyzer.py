a=int(input("Start: "))
b=int(input("End: "))
print("Number Prime Perfect Armstrong Palindrome Digit Sum Digits Binary")
for n in range(a,b+1):
    if n<2:
        prime="No"
    else:
        prime="Yes"
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                prime="No"
                break
    s=str(n)
    ds=sum(int(x) for x in s)
    digits=len(s)
    binary=""
    x=n
    if x==0:
        binary="0"
    else:
        while x>0:
            binary=str(x%2)+binary
            x//=2
    perfect="No"
    if n>1:
        total=0
        for i in range(1,n):
            if n%i==0:
                total+=i
        if total==n:
            perfect="Yes"
    power=len(s)
    armstrong="Yes"
    total=0
    for x in s:
        total+=int(x)**power
    if total!=n:
        armstrong="No"
    palindrome="Yes" if s==s[::-1] else "No"
    print(n,prime,perfect,armstrong,palindrome,ds,digits,binary)