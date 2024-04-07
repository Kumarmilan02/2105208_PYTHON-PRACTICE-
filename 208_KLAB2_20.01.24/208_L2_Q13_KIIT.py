#WAPP to enter your marks of any 5 courses of 2 semesters through keyboard print the 
#corresponding grade.  
#Calculate SGPA for each semester and overall CGPA. 

#  Number of semesters
num_semesters = int(input("Enter the number of semesters: "))

# Initialize variables for overall CGPA calculation
total_credits_all_semesters = 0
total_credit_points_all_semesters = 0

# Iterate through each semester
for semester in range(1, num_semesters + 1):
    print(f"\n--- Semester {semester} ---")
    total_credits_semester = 0
    total_credit_points_semester = 0

    # Iterate through each course in the semester
    for course in range(1, 6):
        marks = float(input(f"Enter marks for Course {course}: "))
        credits = int(input(f"Enter credits for Course {course}: "))

        # Calculate grade and credit points
        if 90 <= marks <= 100:
            grade = 'O'
            points = 10
        elif 80 <= marks <= 89:
            grade = 'E'
            points = 9
        elif 70 <= marks <= 79:
            grade = 'A'
            points = 8
        elif 60 <= marks <= 69:
            grade = 'B'
            points = 7
        elif 50 <= marks <= 59:
            grade = 'C'
            points = 6
        elif 40 <= marks <= 49:
            grade = 'D'
            points = 5
        else:
            grade = 'F'
            points = 2

        # Calculate credit points for the course
        credit_points = credits * points

        # Update total credit points and credits for the semester
        total_credit_points_semester += credit_points
        total_credits_semester += credits

        print(f"Grade for Course {course}: {grade}, Credit Points: {credit_points}")

    # Calculate SGPA for the semester
    sgpa = total_credit_points_semester / total_credits_semester
    print(f"SGPA for Semester {semester}: {sgpa:.2f}")

    # Update overall CGPA variables
    total_credit_points_all_semesters += total_credit_points_semester
    total_credits_all_semesters += total_credits_semester

# Calculate CGPA
cgpa = total_credit_points_all_semesters / total_credits_all_semesters
print(f"\nOverall CGPA: {cgpa:.2f}")
