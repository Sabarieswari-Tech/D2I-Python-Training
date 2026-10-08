invalid=0
while True:
    n=int(input())
    if n<1 or n>100:
        print("Invalid input")
        invalid+=1
        continue
    break
print("Accepted value:",n)
print("Invalid attempts:",invalid)