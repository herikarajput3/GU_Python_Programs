# Function to calculate total marks
def calculate_total(marks):
    total = 0
    for mark in marks:
        total += mark;
    return total

# Function to calculate percentage
def calculate_percentage(total, num_of_marks):
    return total/num_of_marks;

# Function to determine grade based on percentage
def determine_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'


marks=[0,0,0,0,0];
for i in range(5):
    marks[i] = float(input("Enter mark " + str(i + 1) + ": "))
    
total = calculate_total(marks)
percentage = calculate_percentage(total, len(marks))
grade = determine_grade(percentage)

print("Marks:",marks)
print("Total:",total)
print("Percentage:",percentage)
print("Grade:",grade) 



