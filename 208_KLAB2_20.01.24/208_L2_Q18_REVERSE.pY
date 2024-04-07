# WAPP to display the reverse of a number entered through keyboard. 

# Program to display the reverse of a number entered through the keyboard

# Input a number
num = int(input("Enter a number: "))
num2=0
while num!=0:
    dig = num%10
    num2=num2*10+dig
    num=num//10
print("Reversed no. is",num2)

# Convert the number to a string and reverse it
#reverse_num = int(str(num)[::-1])

# Display the result
#print(f"The reverse of {num} is: {reverse_num}")
