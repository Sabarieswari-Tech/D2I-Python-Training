p=float(input())
r=float(input())
t=float(input())
if p<0 or r<0 or t<0:
    print("Invalid input")
else:
    si=p*r*t/100
    total=p+si
    print(f"Principal     : {p:.2f}")
    print(f"Rate          : {r:.2f}%")
    print(f"Time          : {t:.2f} years")
    print(f"Simple Interest: {si:.2f}")
    print(f"Total Amount  : {total:.2f}")