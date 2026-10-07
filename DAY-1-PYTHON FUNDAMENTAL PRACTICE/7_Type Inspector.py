x=input()
print("Original value type:",type(x).__name__)
try:
    i=int(x)
    print("Integer value :",i)
    print("Integer type  :",type(i).__name__)
except:
    print("Invalid integer conversion")
try:
    f=float(x)
    print("Float value   :",f)
    print("Float type    :",type(f).__name__)
except:
    print("Invalid float conversion")