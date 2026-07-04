num=[10,20,30,69,14]
while True:
    search=int(input("Enter the number to search: "))
    found=False
    for n in num:
        if n==search:
            found=True
            break
    if found:
        print("Milgya")
        break
    else:
        print("Nahi Milgya")