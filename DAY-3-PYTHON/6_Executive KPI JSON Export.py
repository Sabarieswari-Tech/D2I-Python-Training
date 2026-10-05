import json

summary_data=[
{"category":"Electronics","total_revenue":2650.0,"avg_revenue":1325.0},
{"category":"Furniture","total_revenue":300.0,"avg_revenue":300.0}
]

def export_kpi_summary(summary_data,top_category,output_filepath):
    data={"status":"SUCCESS","top_category":top_category,"metrics":summary_data}
    with open(output_filepath,"w") as f:
        json.dump(data,f,indent=2)
    with open(output_filepath) as f:
        return json.load(f)

print(export_kpi_summary(summary_data,"Electronics","kpi_report.json"))