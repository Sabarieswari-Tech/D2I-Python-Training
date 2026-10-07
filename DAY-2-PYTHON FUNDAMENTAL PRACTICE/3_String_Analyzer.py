s=input()
rev=""
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
print("Loop Reverse:",rev)
print("Slice Reverse:",s[::-1])
clean=""
for ch in s:
    if ch!=" ":
        clean+=ch.lower()
rev=""
for i in range(len(clean)-1,-1,-1):
    rev+=clean[i]
if clean==rev:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")
vowels=0
consonants=0
digits=0
for ch in s.lower():
    if ch in "aeiou":
        vowels+=1
    elif ch.isalpha():
        consonants+=1
    elif ch.isdigit():
        digits+=1
print("Vowels:",vowels)
print("Consonants:",consonants)
print("Digits:",digits)