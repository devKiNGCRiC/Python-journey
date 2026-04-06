age = int(input("Enter Age : "))
weight = int(input("Enter Weight : "))

if age < 18 or weight < 40 or age > 120 or weight > 85:
    print("Not Eligible for Donation")
else:
    print("Eligible for Donation")