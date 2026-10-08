n=int(input())
a=list(map(int,input().split()))
p=ne=z=ev=od=both=only3=only5=neither=0
for x in a:
    if x>0:p+=1
    elif x<0:ne+=1
    else:z+=1
    if x!=0:
        if x%2==0:ev+=1
        else:od+=1
    if x%3==0 and x%5==0:both+=1
    elif x%3==0:only3+=1
    elif x%5==0:only5+=1
    else:neither+=1
print("Positive:",p)
print("Negative:",ne)
print("Zero:",z)
print("Even:",ev)
print("Odd:",od)
print("Divisible by both 3 and 5:",both)
print("Divisible only by 3:",only3)
print("Divisible only by 5:",only5)
print("Divisible by neither:",neither)