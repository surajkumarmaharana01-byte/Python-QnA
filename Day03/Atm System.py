print("===== ATM SYSTEM =====")

pin = "1234"
balance = 5000

while True:

    user_pin = input("Enter ATM PIN: ")

    if user_pin == pin:

        print("Login Successful")

        print("""
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
""")

        choice = int(input("Enter Choice: "))

        match choice:

            case 1:
                print("Current Balance =", balance)

            case 2:
                amount = int(input("Enter Deposit Amount: "))
                balance = balance + amount
                print("New Balance =", balance)

            case 3:
                amount = int(input("Enter Withdraw Amount: "))

                if amount <= balance:
                    balance = balance - amount
                    print("Remaining Balance =", balance)
                else:
                    print("Insufficient Balance")

            case 4:
                print("Thank You")
                break

            case _:
                print("Invalid Choice")

        break

    else:
        print("Wrong PIN")