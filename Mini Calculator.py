print("===== MINI CALCULATOR =====")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
""")

choice = int(input("Enter Your Choice: "))

match choice:

    case 1:
        print("Answer =", num1 + num2)

    case 2:
        print("Answer =", num1 - num2)

    case 3:
        print("Answer =", num1 * num2)

    case 4:
        if num2 != 0:
            print("Answer =", num1 / num2)
        else:
            print("Division by zero is not possible")

    case _:
        print("Invalid Choice")