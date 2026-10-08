s=input("Message: ")
n=int(input("Shift: "))
e=""
for c in s:
    if c.isupper():
        e+=chr((ord(c)-65+n)%26+65)
    elif c.islower():
        e+=chr((ord(c)-97+n)%26+97)
    else:
        e+=c
d=""
for c in e:
    if c.isupper():
        d+=chr((ord(c)-65-n)%26+65)
    elif c.islower():
        d+=chr((ord(c)-97-n)%26+97)
    else:
        d+=c
print("Encrypted:",e)
print("Decrypted:",d)