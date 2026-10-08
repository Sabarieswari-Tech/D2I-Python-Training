while True:
    print("1. Celsius to Fahrenheit")
    print("2. Kilometres to Miles")
    print("3. Kilograms to Pounds")
    print("4. Exit")
    c=int(input())
    if c==1:
        x=float(input())
        print("Fahrenheit:",(x*9/5)+32)
    elif c==2:
        x=float(input())
        print("Kilometres to Miles:",round(x*0.621371,2))
    elif c==3:
        x=float(input())
        print("Kilograms to Pounds:",round(x*2.20462,2))
    elif c==4:
        print("Exit")
        break
    else:
        print("Invalid choice")
        continue