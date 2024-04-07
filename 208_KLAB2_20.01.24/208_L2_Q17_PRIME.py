# Program to print the sum of all prime numbers between 1 to n

# Input value of n
n = int(input("Enter the value of n: "))

# Initialize variables
sum_primes = 0

# Iterate through numbers from 2 to n
for num in range(2, n + 1):
    is_prime = True

    # Check if num is prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    # If num is prime, add it to the sum
    if is_prime:
        sum_primes += num

# Display the sum of prime numbers
print(f"The sum of prime numbers between 1 to {n} is: {sum_primes}")
