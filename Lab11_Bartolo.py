grades = []
passed_students = []
valid_input = True  

while True:
    grade = input("Enter a grade (or type 'done' to stop): ")

    if grade.lower() == 'done':
        break
    if not grade.isdigit():
        print("Error: Please enter a numeric grade.")
    else:
        grade = int(grade)
        if grade <= 40:
            print("Invalid Data")
            valid_input = False  
            break  
        else:
            grades.append(grade)
            if grade >= 75:
                passed_students.append(grade)

if valid_input:
    if grades:
        
        average = sum(grades) / len(grades)
        passing_percentage = (len(passed_students) / len(grades)) * 100
        print(f"The average grade is: {average:.2f}")
        print(f"The passing percentage is: {passing_percentage:.2f}%")
        print(f"The number of students who passed: {len(passed_students)}")
        print(f"Grades: {grades}")
    else:    
        print("No grades were entered")
