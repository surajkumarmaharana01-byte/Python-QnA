pw="Suraj@123"
attempts=0

while attempts<3:
    n=input("Enter ur Password = ")

    if n==pw:
        print("Login Successful")
        break
    else:
        attempts+=1

        if attempts==3:
            print("Card Blocked")
        else:
            print("Wrong Password")
            print("Attempts Left:",3-attempts)