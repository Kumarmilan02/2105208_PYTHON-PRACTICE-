#WAPP to findout the distance between two coordinates (x1, y1) & (x2, y2).

import math

print("CO-ORDINATE - 1")
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

print("\nCO-ORDINATE - 2")
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
d = math.sqrt(((x2-x1) * (x2-x1))+((y2-y1) * (y2-y1)))
print("\nDistance between the coordinates: ", d)

