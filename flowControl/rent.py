month = int(input("Enter the Valid Month Number (1-12) : "))
rentPerDay = float(input("Enter the Per day Rent of the Room : "))
numOfDays = int(input("Enter The Number Of Days Stay in the Hostel : "))

if month > 12 or month < 1:
    print("Invalid Month Number")
else:
    if month == 4 or month == 5:
        increasedRent = rentPerDay * 20/100
        print(f'Rs.{(increasedRent+rentPerDay)*numOfDays :.2f}')
    else:
        print(f'Rs.{rentPerDay*numOfDays:.2f}')