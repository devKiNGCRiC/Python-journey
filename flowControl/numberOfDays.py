month = int(input("Enter the Month Number (1-12) : "))
if month > 12 or month < 1:
    print("Invalid Month Number")
else:
    if month == 2:
        print("28/29 Days")
    if month == 4 or month == 6 or month == 9 or month == 11:
        print("30 Days")
    else:
        print("31 Days")