import re

text="Contact support at ravi.kumar@techcorp.in or admin@sales.co. Direct helpline: +91 9876543210 or call 8765432109."

emails=re.findall(r'[\w.-]+@[\w.-]+\.\w+',text)
phones=re.findall(r'(?:\+91\s?)?[6-9]\d{9}',text)

print({"emails":emails,"phones":phones})