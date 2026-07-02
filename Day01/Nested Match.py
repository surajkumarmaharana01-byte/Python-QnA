language = int(input("Choose Language\n1. English\n2. Hindi\n3. Odia\nEnter choice: "))

match language:
    case 1:
        greeting = int(input("1. Hello\n2. Good Morning\n3. Thank You\nEnter choice: "))

        match greeting:
            case 1:
                print("Hello")
            case 2:
                print("Good Morning")
            case 3:
                print("Thank You")
            case _:
                print("Invalid Greeting")

    case 2:
        greeting = int(input("1. Namaste\n2. Suprabhat\n3. Dhanyawad\nEnter choice: "))

        match greeting:
            case 1:
                print("Namaste")
            case 2:
                print("Suprabhat")
            case 3:
                print("Dhanyawad")
            case _:
                print("Invalid Greeting")

    case 3:
        greeting = int(input("1. Namaskar\n2. Suprabhat\n3. Dhanyabad\nEnter choice: "))

        match greeting:
            case 1:
                print("Namaskar")
            case 2:
                print("Suprabhat")
            case 3:
                print("Dhanyabad")
            case _:
                print("Invalid Greeting")

    case _:
        print("Invalid Language")