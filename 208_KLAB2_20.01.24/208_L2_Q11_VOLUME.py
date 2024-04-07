# WAPP to find Volume and Surface Area of Cylinder. 
# Input radius and height of the cylinder from the user
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate volume and surface area of the cylinder
pi = 3.14159

# Volume of the cylinder = π * r^2 * h
volume = pi * radius**2 * height

# Surface area of the cylinder = 2 * π * r * (r + h)
surface_area = 2 * pi * radius * (radius + height)

# Display the results
print(f"\nVolume of the cylinder: {volume:.2f} cubic units")
print(f"Surface area of the cylinder: {surface_area:.2f} square units")
