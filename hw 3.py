a=int(input("Enter a number: "))
if a>=0 and a<=9:
    print("The number is a single-digit number.")
elif a>=10 and a<=99:
    print("The number is a two-digit number.")
elif a>=100 and a<=999:
    print("The number is a three-digit number.")
elif a>=1000 and a<=9999:
    print("The number is a four-digit number.")
elif a>=10000 and a<=99999:
    print("The number is a five-digit number.")
elif a>=100000 and a<=999999: 
    print("The number is a six-digit number.")
else:
    print("The number is greater than six digits.")