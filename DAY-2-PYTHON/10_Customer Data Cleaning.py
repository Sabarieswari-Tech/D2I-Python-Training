data=[
"Asha, Chennai, 25",
"Bala, chennai, 30",
"asha, Chennai, 25",
"Charan, Bangalore, 28",
"Bala, Chennai, 30"
]

result=[]
seen=set()

for record in data:
    name,city,age=[x.strip() for x in record.split(",")]
    name=name.title()
    city=city.title()
    age=int(age)
    key=(name,city,age)
    if key not in seen:
        seen.add(key)
        result.append({"name":name,"city":city,"age":age})

print(result)


