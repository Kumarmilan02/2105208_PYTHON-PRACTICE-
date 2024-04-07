#WAPP to sum the following series    S=1+(1+2)+(1+2+3)+...+(1+2+3+...+n)


# Program to sum the series S=1+(1+2)+(1+2+3)+...+(1+2+3+...+n)

# Input value of n
n = int(input("Enter a number (n): "))

# Initialize sum
sum_series = 0

# Loop to calculate the sum of the series
for i in range(1, n + 1):
    sum_series += sum(range(1, i + 1))

# Display the result
print(f"The sum of the series is: {sum_series}")
