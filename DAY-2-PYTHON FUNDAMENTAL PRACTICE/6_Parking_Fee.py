entry=input()
exit=input()
eh,em=map(int,entry.split(":"))
xh,xm=map(int,exit.split(":"))
start=eh*60+em
end=xh*60+xm
if end<start:
    end+=24*60
duration=end-start
hours=duration//60
minutes=duration%60
billable=hours
if minutes>0:
    billable+=1
if billable<=1:
    fee=30
else:
    fee=30+(billable-1)*20
print(f"Parking Duration: {hours} hours {minutes} minutes")
print("Billable Hours:",billable)
print("Parking Fee: ₹",fee)