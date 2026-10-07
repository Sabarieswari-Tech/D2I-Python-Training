items=[]
while True:
    x=input()
    if x.lower()=="done":
        break
    items.append(float(x))
subtotal=sum(items)
if subtotal>=1000:
    discount=subtotal*0.10
elif subtotal>=500:
    discount=subtotal*0.05
else:
    discount=0
tax=(subtotal-discount)*0.18
final=subtotal-discount+tax
print("Item Price")
for i,p in enumerate(items,1):
    print(f"Item {i} {p:.2f}")
print("------------")
print(f"Subtotal {subtotal:.2f}")
print(f"Discount {discount:.2f}")
print(f"Tax {tax:.2f}")
print(f"Final {final:.2f}")