name=input()
units=int(input())
if units<=100:
    amount=units*3
elif units<=200:
    amount=100*3+(units-100)*4
else:
    amount=100*3+100*4+(units-200)*5
print("Customer :",name)
print("Units :",units)
print(f"Amount : ₹{amount:.2f}")