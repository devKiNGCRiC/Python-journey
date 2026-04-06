year = int(input("Enter the Year : "))
print("Leap Year" if year%4==0 and year%100!=0 or year%400==0 else "Not a Leap Year")