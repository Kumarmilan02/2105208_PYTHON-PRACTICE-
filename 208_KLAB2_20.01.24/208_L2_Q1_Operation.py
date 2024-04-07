# ''' Write a Python program(WAPP) to input any two integers, and provide a menu to the 
# user to select any of the options as add, subtract, multiply, divide and display the result 
# accordingly.  '''

def add(a, b):
    sum = a + b
    print(a, "+", b, "=", sum)

def subtract(a, b):
    difference = a - b
    print(a, "-", b, "=", difference)

def multiply(a, b):
    product = a * b
    print(a, "x", b, "=", product)

def divide(a, b):
    division = a / b
    print(a, "/", b, "=", division)

print("MENU - DRIVEN PROGRAM")

while True:
    print("\nMENU")
    print("1. Sum of two Numbers")
    print("2. Difference between two Numbers")
    print("3. Product of two Numbers")
    print("4. Division of two Numbers")
    print("5. Exit")
    choice = int(input("\nEnter the Choice: "))

    if choice == 1:
        print("\nADDITION\n")
        a = int(input("First Number: "))
        b = int(input("Second Number: "))
        add(a, b)

    elif choice == 2:
        print("\nSUBTRACTION\n")
        a = int(input("First Number: "))
        b = int(input("Second Number: "))
        subtract(a, b)

    elif choice == 3:
        print("\nMULTIPLICATION\n")
        a = int(input("First Number: "))
        b = int(input("Second Number: "))
        multiply(a, b)

    elif choice == 4:
        print("\nDIVISION\n")
        a = int(input("First Number: "))
        b = int(input("Second Number: "))
        divide(a, b)

    elif choice == 5:
        print("\nEXIT\n")
        break

    else:
        print("Please Provide a valid Input!")
