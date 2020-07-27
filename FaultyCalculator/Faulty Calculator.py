operator = input("Enter the type of operation: ")
num_1 = int(input("Enter number : "))
num_2 = int(input("Enter number : "))

if operator == "+":
    if ( num_1 == 56 and num_2 == 9 ) :
        print("77")
    else:
        print(num_1 + num_2)
elif operator == "*":
    if (num_1 == 45 and num_2 == 3):
        print("555")
    else:
        print(num_1 * num_2)
elif operator == "/":
    if (num_1 == 56 and num_2 == 6):
        print("4")
    else:
        print(int(num_1 / num_2))

