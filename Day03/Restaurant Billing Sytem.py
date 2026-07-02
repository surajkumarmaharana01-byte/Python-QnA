print("===== RESTAURANT BILLING SYSTEM =====")

print("""
1. Burger - ₹120
2. Pizza - ₹250
3. Sandwich - ₹100
4. Cold Drink - ₹50
""")

choice = int(input("Enter Your Choice: "))
quantity = int(input("Enter Quantity: "))

match choice:

    case 1:
        item = "Burger"
        price = 120

    case 2:
        item = "Pizza"
        price = 250

    case 3:
        item = "Sandwich"
        price = 100

    case 4:
        item = "Cold Drink"
        price = 50

    case _:
        print("Invalid Choice")
        exit()

total = price * quantity

print("\n===== BILL =====")
print("Item :", item)
print("Price :", price)
print("Quantity :", quantity)
print("Total Bill : ₹", total)

if total >= 500:
    print("Discount : ₹50")
    total = total - 50

print("Final Bill : ₹", total)
print("Thank You! Visit Again.")