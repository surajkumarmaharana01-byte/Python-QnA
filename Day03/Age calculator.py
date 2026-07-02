print("===== AGE CALCULATOR =====")

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

print("\n===== RESULT =====")
print("Name:", name)
print("Age:", age)

if age >= 18:
    print("Voting Eligibility : Eligible")
else:
    print("Voting Eligibility : Not Eligible")

if age >= 18:
    print("Driving Eligibility : Eligible")
else:
    print("Driving Eligibility : Not Eligible")

if age >= 60:
    print("Senior Citizen : Yes")
else:
    print("Senior Citizen : No")

print("Thank You!")