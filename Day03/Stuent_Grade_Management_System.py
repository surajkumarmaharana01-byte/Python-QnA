print("===== STUDENT GRADE MANAGEMENT SYSTEM =====")

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

m1 = int(input("Enter Marks of Subject 1: "))
m2 = int(input("Enter Marks of Subject 2: "))
m3 = int(input("Enter Marks of Subject 3: "))
m4 = int(input("Enter Marks of Subject 4: "))
m5 = int(input("Enter Marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\n===== RESULT =====")
print("Name:", name)
print("Roll Number:", roll)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if percentage >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")