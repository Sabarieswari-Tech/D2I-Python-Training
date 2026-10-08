p=input()
u=l=d=s=0
for x in p:
    if x.isupper():u=1
    elif x.islower():l=1
    elif x.isdigit():d=1
    else:s=1
if len(p)>=8 and u and l and d and s:
    print("Valid password")
else:
    print("Invalid password")
print("Uppercase:","Present" if u else "Missing")
print("Lowercase:","Present" if l else "Missing")
print("Digit:","Present" if d else "Missing")
print("Special character:","Present" if s else "Missing")
print("Minimum length:","Satisfied" if len(p)>=8 else "Not satisfied")