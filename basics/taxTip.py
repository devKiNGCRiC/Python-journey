billAmt = int(input("Enter Bill Amount : "))
tax = billAmt * 18/100
tip = billAmt * 5/100
print (f'The Tax is : {tax}')
print (f'The Tip is : {tip}')
print (f'Total Bill with Tax and Tip : {(billAmt + tax + tip):.2f}')