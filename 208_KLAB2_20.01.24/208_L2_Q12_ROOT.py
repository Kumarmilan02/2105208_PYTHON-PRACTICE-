#WAPP to find the roots of a quadratic equation ax^2+bx+c=0

# Program to find the roots of a quadratic equation ax^2 + bx + c = 0

# Input coefficients a, b, and c
a = float(input("Enter the coefficient 'a': "))
b = float(input("Enter the coefficient 'b': "))
c = float(input("Enter the coefficient 'c': "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the nature of roots
if discriminant > 0:
    # Two distinct real roots
    root1 = (-b + (discriminant)**0.5) / (2*a)
    root2 = (-b - (discriminant)**0.5) / (2*a)
    print(f"The roots are real and distinct: {root1}, {root2}")
elif discriminant == 0:
    # One real root (double root)
    root = -b / (2*a)
    print(f"The root is real and repeated: {root}")
else:
    # Complex roots
    real_part = -b / (2*a)
    imaginary_part = (abs(discriminant)**0.5) / (2*a)
    root1 = complex(real_part, imaginary_part)
    root2 = complex(real_part, -imaginary_part)
    print(f"The roots are complex conjugates: {root1}, {root2}")
