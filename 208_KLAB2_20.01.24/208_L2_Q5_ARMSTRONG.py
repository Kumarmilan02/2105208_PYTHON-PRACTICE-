#WAPP to check given number is Armstrong or not.

num = int(input("Enter a number: "))
n = len(str(num))
temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** n
    temp //= 10
if total == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
