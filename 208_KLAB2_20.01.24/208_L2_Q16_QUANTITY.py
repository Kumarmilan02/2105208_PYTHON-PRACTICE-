# Program to convert a quantity in meters to its equivalent kilometer and meter

# Input quantity in meters
quantity_in_meters = int(input("Enter a quantity in meters: "))

# Calculate the equivalent kilometer and meter
kilometer = quantity_in_meters // 1000
remaining_meter = quantity_in_meters % 1000

# Display the result
print(f"{quantity_in_meters} meters = {kilometer} Km and {remaining_meter} meters.")
