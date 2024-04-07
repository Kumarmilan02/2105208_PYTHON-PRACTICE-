#WAPP to find LCM of 2 numbers using while loop. 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
greater = max(num1, num2)
lcm = greater
while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        print(f"The LCM of {num1} and {num2} is {lcm}.")
        break
    lcm += greater
