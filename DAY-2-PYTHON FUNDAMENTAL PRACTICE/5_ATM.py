amount=int(input())
if amount%10!=0 or amount>20000:
    print("Invalid withdrawal amount")
else:
    n500=amount//500
    amount%=500
    n200=amount//200
    amount%=200
    n100=amount//100
    amount%=100
    n50=amount//50
    amount%=50
    n10=amount//10
    print("₹500 notes:",n500)
    print("₹200 notes:",n200)
    print("₹100 notes:",n100)
    print("₹50 notes:",n50)
    print("₹10 notes:",n10)
    print("Total Notes:",n500+n200+n100+n50+n10)