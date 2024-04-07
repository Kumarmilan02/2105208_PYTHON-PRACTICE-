# High Radius Company decided to give bonus of 10% to employee if his/her year of service 
# is more than 5 years. 
# • Enter salary and year of service from keyboard and print the net bonus amount. 
# • Determine oldest and youngest among 3 employees by taking input(from user) of  
# their age. 


# Program to calculate bonus based on years of service

# Input salary and years of service
salary = float(input("Enter the salary: "))
years_of_service = int(input("Enter the years of service: "))

# Calculate bonus
if years_of_service > 5:
    bonus_percentage = 10
    bonus_amount = (bonus_percentage / 100) * salary
    print(f"Net Bonus Amount: {bonus_amount}")
else:
    print("No bonus for less than 5 years of service.")
