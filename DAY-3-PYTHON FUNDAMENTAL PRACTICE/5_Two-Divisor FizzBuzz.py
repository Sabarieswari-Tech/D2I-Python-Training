n=int(input("N: "))
d1=int(input("Divisor 1: "))
w1=input("Word 1: ")
d2=int(input("Divisor 2: "))
w2=input("Word 2: ")
for i in range(1,n+1):
    if i%d1==0 and i%d2==0:
        print(w1+w2)
    elif i%d1==0:
        print(w1)
    elif i%d2==0:
        print(w2)
    else:
        print(i)