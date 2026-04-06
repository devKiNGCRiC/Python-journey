withdrawal = float(input("Enter WithDrawal Amount : "))
ini_amt = float(input("Enter Initial Balance : "))

if ini_amt > withdrawal:
    cur_bal = ini_amt - withdrawal - 0.5
    print(f'Current Balance : {cur_bal:.2f}\nInitial Balance : {ini_amt:.2f}')
else:
    print(f'Invalid Withdrawal Request\nInitial Balance : {ini_amt:.2f}')