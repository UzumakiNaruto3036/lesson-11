print("this is a right angled triangle")
n=int(input("enter a integer: "))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()