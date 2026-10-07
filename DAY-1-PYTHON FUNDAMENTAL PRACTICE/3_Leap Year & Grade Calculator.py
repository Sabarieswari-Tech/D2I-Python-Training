year=int(input())
marks=int(input())
if marks<0 or marks>100:
    print("Invalid marks. Enter a value between 0 and 100.")
else:
    if year%400==0 or (year%4==0 and year%100!=0):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")
    if marks>=85:
        grade="A"
    elif marks>=70:
        grade="B"
    elif marks>=60:
        grade="C"
    elif marks>=50:
        grade="D"
    else:
        grade="F"
    print("Grade:",grade)