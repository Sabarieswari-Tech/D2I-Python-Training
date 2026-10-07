x=int(input())
sign=1
if x<0:
    sign=-1
    x=-x
rev=0
while x>0:
    rev=rev*10+x%10
    x//=10
print(sign*rev)