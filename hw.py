a=int(input("Enter a decimal number: "))
binary=""
if a==0:
    print("Enter a value greater than 0")
else:
    while a>0:
        remainder=a%2
        binary=str(remainder)+binary
        a=a//2
    print("the binary conversion is:",binary)