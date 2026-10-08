a=int(input("Number 1: "))
b=int(input("Number 2: "))
def convert(n,base):
    chars="0123456789ABCDEF"
    result=""
    while n>0:
        result=chars[n%base]+result
        n//=base
    return result or "0"
x=a
while x>0:
    if b%x==0:
        gcd=x
        break
    x-=1
lcm=a*b//gcd
print("Binary:",convert(a,2))
print("Octal:",convert(a,8))
print("Hexadecimal:",convert(a,16))
print("GCD:",gcd)
print("LCM:",lcm)