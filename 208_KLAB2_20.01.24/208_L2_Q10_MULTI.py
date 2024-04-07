#WAPP to find the multiplication table of any number using for loop. 

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
