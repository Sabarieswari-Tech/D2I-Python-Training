age = int(input("Enter your age: "))

voting = "Eligible" if age >= 18 else "Not Eligible"
discount = "Senior Citizen Discount" if age >= 60 else "No Discount"

print("Voting:", voting)
print(discount)
