text="Python is easy and Python is powerful"

result={}
for word in text.lower().split():
    result[word]=result.get(word,0)+1

print(result)