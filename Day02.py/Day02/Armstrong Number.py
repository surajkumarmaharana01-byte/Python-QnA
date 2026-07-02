num = int(input("Enter number: "))

original = num
total = 0

while num > 0:
    digit = num % 10
    total = total + digit ** 3
    num = num // 10

if original == total:
    print("Armstrong Number")
else:
    print("Not Armstrong")