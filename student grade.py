student = ["nader" , "amir" , "amira" , "john"]
grader= [80,45,75,78]
passed = 0 
failed = 0
ranking = sorted(zip(student , grader) , key=lambda grade : grade[1] , reverse=True)
for rank , (name,grade) in enumerate(ranking , start=1):
      if grade >= 90 :
          print(f"{rank} congratulation {name.title()} your grade is : {grade} it's mean exillant!")
          passed+=1
      elif grade >= 80 :
          print(f"{rank} congratulation {name.title()} your grade is : {grade} it's mean very good!")
          passed+=1
      elif grade >= 70 :
          print(f"{rank} congratulation {name.title()} your grade is : {grade} it's mean good!")
          passed+=1 
      elif grade >=  60 : 
          print(f"{rank} congratulation {name.title()} your grade is : {grade} it's mean pass!")      
          passed+=1
      else :
          print(f"{rank} study hard  {name.title()} your grade is : {grade} it's mean failed!")
          failed+=1          
def avg(x):
    average = sum(x) / len(x)
    return average
average = avg(grader)
print(f"the average is : {average}")
print(f"the highest grade is : {max(grader)}")
print(f"the lowest grade is : {min(grader)}")
print(f"passed student : {passed}")
print(f"failed student : {failed}")
print(ranking)
#-----------------------------------------------------------------------------------------------------------------------
students = [
    {"name": "nader", "grade": 80},
    {"name": "amir", "grade": 45},
    {"name": "amira", "grade": 75},
    {"name": "john", "grade": 78}
]

passed = 0
failed = 0

# Sort students by grade
ranking = sorted(
    students,
    key=lambda student: student["grade"],
    reverse=True
)

# Display ranking and evaluate grades
for rank, student in enumerate(ranking, start=1):#enumerate give a number depending on his order 
    name = student["name"].title()
    grade = student["grade"]

    if grade >= 90:
        message = "Excellent"
        passed += 1
    elif grade >= 80:
        message = "Very Good"
        passed += 1
    elif grade >= 70:
        message = "Good"
        passed += 1
    elif grade >= 60:
        message = "Pass"
        passed += 1
    else:
        message = "Failed"
        failed += 1

    print(f"{rank}. {name} - {grade} - {message}")

# Analyze grades
def analyze_grades(grades):
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)

    return average, highest, lowest

grades = [student["grade"] for student in students]

average, highest, lowest = analyze_grades(grades)

print("\n--- Summary ---")
print(f"Average: {average:.2f}") #show average in 2 decimal number
print(f"Highest grade: {highest}")
print(f"Lowest grade: {lowest}")
print(f"Passed students: {passed}")
print(f"Failed students: {failed}")

