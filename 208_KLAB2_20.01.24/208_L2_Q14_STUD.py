#  A student will not be allowed to sit in exam if his/her attendence is less than 70%. 
# Take following input from user: 
# • Number of classes held  
# • Number of classes attended 
# Print percentage of class attended and check the student is allowed to sit in exam or not.


# Program to check if a student is allowed to sit in the exam based on attendance

# Input number of classes held and attended
classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

# Calculate attendance percentage
attendance_percentage = (classes_attended / classes_held) * 100

# Check eligibility to sit in the exam
if attendance_percentage >= 70:
    print(f"Attendance Percentage: {attendance_percentage}%")
    print("The student is allowed to sit in the exam.")
else:
    print(f"Attendance Percentage: {attendance_percentage}%")
    print("The student is not allowed to sit in the exam.")
