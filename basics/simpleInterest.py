amount = int(input("Enter Principle Amount : "))
rate = float(input("Enter Rate of Interest : "))
time = int(input("Total Time in Years : "))

si = (amount*rate*time)/100
totalAmount = amount+si

print(f'Simple Interest after {time} years : ${si:.2f}')
print(f'Total Amount after {time} years : ${totalAmount:.2f}')