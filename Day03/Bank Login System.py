print("===== BANK LOGIN SYSTEM =====")

username = "Suraj Maharana"
password = "Suraj@123"
otp = "1234"

user = input("Enter Username: ")

if user == username:

    pwd = input("Enter Password: ")

    if pwd == password:

        print("Password Verified")

        user_otp = input("Enter OTP: ")

        if user_otp == otp:
            print("Login Successful")
            print("Welcome to Indian Bank")
        else:
            print("Invalid OTP")

    else:
        print("Wrong Password")

else:
    print("Invalid Username")