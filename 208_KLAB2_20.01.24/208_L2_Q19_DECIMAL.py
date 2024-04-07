# WAPP to convert a decimal number into its equivalent number with base b.  
# Decimal number and b are the user input. 

# Program to convert a decimal number into its equivalent number with base b

# Input decimal number and base
decimal_number = int(input("Enter a decimal number: "))
base = int(input("Enter the base (b): "))

# Validate base
if base < 2:
    print("Base must be 2 or greater.")
else:
    # Initialize variables
    result = ""
    quotient = decimal_number
    
    # Perform conversion
    while quotient > 0:
        remainder = quotient % base
        quotient = quotient // base
        result = str(remainder) + result

    print(f"The equivalent number in base {base} is: {result}")
