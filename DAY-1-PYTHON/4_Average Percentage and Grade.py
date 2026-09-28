m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

average = (m1 + m2 + m3) / 3

print("Average Percentage =", average)

if average >= 90:
    print("Grade A+")
elif average >= 75:
    print("Grade A")
elif average >= 50:
    print("Grade B")
else:
    print("Fail")
