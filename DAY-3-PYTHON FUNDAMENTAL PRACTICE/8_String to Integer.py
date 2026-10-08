s=input()
i=0
while i<len(s) and s[i]==" ":
    i+=1
sign=1
if i<len(s) and (s[i]=="+" or s[i]=="-"):
    if s[i]=="-":
        sign=-1
    i+=1
num=0
while i<len(s) and s[i].isdigit():
    num=num*10+ord(s[i])-ord("0")
    i+=1
print(sign*num)