n = int(input("Enter the number of rows:"))
boolean = input("Enter True or False:")

if bool:
    for i in range(0, n):
        for j in range(i + 1):
            print("*", end=" ")
        print("")
else:
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print("")
