n=int(input("Transactions: "))
a=[]
rejected=0
for i in range(n):
    try:
        x=float(input())
        if x<0:
            rejected+=1
        else:
            a.append(x)
    except ValueError:
        rejected+=1
if a:
    print("Successful Transactions:",len(a))
    print("Total Amount: ₹"+f"{sum(a):.2f}")
    print("Highest Transaction: ₹"+f"{max(a):.2f}")
    print("Lowest Transaction: ₹"+f"{min(a):.2f}")
    print("Average Transaction: ₹"+f"{sum(a)/len(a):.2f}")
else:
    print("Successful Transactions: 0")
    print("Total Amount: ₹0.00")
print("Rejected Transactions:",rejected)