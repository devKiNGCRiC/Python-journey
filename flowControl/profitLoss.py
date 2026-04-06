cost = int(input("Enter Cost Price : "))
sell = int(input("Enter Selling Price : "))

if cost < sell:
    print("PROFIT")
elif cost == sell:
    print("NO PROFIT NO LOSS")
else:
    print("LOSS")