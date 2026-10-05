records=[
("Asha",85,78,92),
("Bala",65,72,70),
("Charan",90,88,95),
("Divya",76,80,84),
("Esha",60,68,72)
]

def analyze_students(records):
    qualified=[]
    topper=""
    highest=0
    for name,a,b,c in records:
        total=a+b+c
        if total/3>=75:
            qualified.append(name)
        if total>highest:
            highest=total
            topper=name
    return {"qualified":qualified,"topper":topper}

print(analyze_students(records))