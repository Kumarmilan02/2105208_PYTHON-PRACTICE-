#Check if a year is a leap year or not
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# The f-string in Python is a way to format strings. 
# It stands for "formatted string literals." With f-strings,
# you can embed expressions inside string literals, using curly braces {}