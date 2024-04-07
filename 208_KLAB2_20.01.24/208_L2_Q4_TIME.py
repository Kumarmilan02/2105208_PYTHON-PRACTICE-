#WAPP to  add two times in  hour, minute & second format entered through the keyboard. 



time1 = input("Enter the first time (HH:MM:SS): ")
time2 = input("Enter the second time (HH:MM:SS): ")

h1, m1, s1 = [int(unit) for unit in time1.split(':')]
h2, m2, s2 = [int(unit) for unit in time2.split(':')]

total_seconds = (h1 + h2) * 3600 + (m1 + m2) * 60 + (s1 + s2)

result_hours, remainder = divmod(total_seconds, 3600)
result_minutes, result_seconds = divmod(remainder, 60)

result_time = f"{result_hours:02d}:{result_minutes:02d}:{result_seconds:02d}"

print(f"The sum of {time1} and {time2} is {result_time}.")

# time1 = input("Enter the first time (HH:MM:SS): ")
# time2 = input("Enter the second time (HH:MM:SS): ")

# h1, m1, s1 = map(int, time1.split(':'))
# h2, m2, s2 = map(int, time2.split(':'))

# total_seconds = (h1 + h2) * 3600 + (m1 + m2) * 60 + (s1 + s2)
# result_time = f"{total_seconds // 3600:02d}:{(total_seconds % 3600) // 60:02d}:{total_seconds % 60:02d}"
# print(f"The sum of {time1} and {time2} is {result_time}.")

#double forward slash ( // ) is the floor division operator.10 // 3 will return 3, because 10 divided by 3 is 3.3333, and rounding that down to the nearest integer gives 3.
# %02d in Python is a string formatting operator that formats an integer to a field of minimum width 2, with zero-padding on the left
# WAPP to add two times in hour, minute & second format entered through the keyboard.

# time1 = input("Enter the first time (HH:MM:SS): ")
# time2 = input("Enter the second time (HH:MM:SS): ")

# h1, m1, s1 = [int(unit) for unit in time1.split(':')]
# h2, m2, s2 = [int(unit) for unit in time2.split(':')]

# total_seconds = (h1 + h2) * 3600 + (m1 + m2) * 60 + (s1 + s2)
# result_time = f"{total_seconds // 3600:02d}:{(total_seconds % 3600) // 60:02d}:{total_seconds % 60:02d}"
# print(f"The sum of {time1} and {time2} is {result_time}.")

