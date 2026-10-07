n=int(input())
num=int(input())
print("Primes:",end=" ")
for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,end=" ")
fact=1
for i in range(1,n+1):
    fact*=i
print("\nFactorial:",fact)
a=0
b=1
print("Fibonacci:",end=" ")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
temp=num
sum=0
while temp>0:
    sum+=temp%10
    temp//=10
print("\nDigit Sum:",sum)
temp=num
rev=0
while temp>0:
    rev=rev*10+temp%10
    temp//=10
print("Reverse:",rev)