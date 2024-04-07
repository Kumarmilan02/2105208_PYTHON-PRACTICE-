# WAPP to find out the factors of a number. 

num = int(input("Enter a number: "))
factors = [i for i in range(1, num + 1) if num % i == 0]
print(f"The factors of {num} are: {factors}")
