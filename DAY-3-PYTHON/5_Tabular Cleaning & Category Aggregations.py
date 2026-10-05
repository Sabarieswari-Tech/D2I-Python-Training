import pandas as pd

sample_sales=[
{"txn_id":"T1","category":"Electronics","price":1000.0,"quantity":2},
{"txn_id":"T2","category":"Furniture","price":300.0,"quantity":1},
{"txn_id":"T3","category":"Electronics","price":None,"quantity":1},
{"txn_id":"T4","category":"Electronics","price":1000.0,"quantity":2}
]

def analyze_sales_data(raw_records):
    df=pd.DataFrame(raw_records).drop_duplicates()
    df["price"]=df.groupby("category")["price"].transform(lambda x:x.fillna(x.mean()))
    df["revenue"]=df["price"]*df["quantity"]
    result=df.groupby("category")["revenue"].agg(["sum","mean"]).reset_index()
    return [(r["category"],r["sum"],r["mean"]) for _,r in result.iterrows()]

print(analyze_sales_data(sample_sales))
