numbers=[10,20,10,30,20,40,30,50]

result=[]
for n in numbers:
    if n not in result:
        result.append(n)

print(result)