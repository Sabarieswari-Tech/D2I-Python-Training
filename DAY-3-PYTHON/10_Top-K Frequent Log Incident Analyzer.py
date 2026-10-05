logs=[
"ERROR: db timeout",
"INFO: user login",
"ERROR: auth failed",
"WARNING: disk low",
"ERROR: lost connection",
"INFO: user logout"
]

def top_k_frequent_logs(logs,k):
    count={}
    for log in logs:
        tag=log.split(":")[0]
        count[tag]=count.get(tag,0)+1
    result=sorted(count,key=lambda x:(-count[x],x))
    return result[:k]

print(top_k_frequent_logs(logs,2))