n=int(input("Students: "))
print("Student Total Average Grade")
for i in range(n):
    name=input()
    marks=input().split()
    try:
        marks=list(map(float,marks))
        if any(x<0 or x>100 for x in marks):
            print(name,"Invalid marks")
            continue
        total=sum(marks)
        avg=total/len(marks)
        if avg>=90:
            grade="A+"
        elif avg>=80:
            grade="A"
        elif avg>=70:
            grade="B"
        elif avg>=60:
            grade="C"
        elif avg>=50:
            grade="D"
        else:
            grade="F"
        print(name,int(total),f"{avg:.2f}",grade)
    except ValueError:
        print(name,"Invalid marks")