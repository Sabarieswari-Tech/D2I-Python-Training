log_records=[
"TXN101,145.50",
"TXN102,invalid_num",
"TXN103,300.00",
"CORRUPTED_LINE",
"TXN104,82.25"
]

def parse_logs(log_records):
    valid=[]
    corrupted=0
    for record in log_records:
        try:
            parts=record.split(",")
            if len(parts)!=2:
                raise ValueError
            valid.append({"id":parts[0].strip(),"value":float(parts[1])})
        except:
            corrupted+=1
    return {"valid":valid,"corrupted_count":corrupted}

print(parse_logs(log_records))