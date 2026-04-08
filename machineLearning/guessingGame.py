low = 1
high = 100

while low <= high:
    mid = (low+high)//2
    print(f'Is your Number is {mid}?')

    answer = input("(higher/lower/correct): ")

    if answer == 'correct':
        print(f'Yay! I guessed it!')
        break
    elif answer == 'higher':
        low = mid + 1
    else:
        high = mid - 1