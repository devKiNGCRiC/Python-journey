str1=str(input("Enter Number of Names : "))
t = int(str1)
for i in range(t):
    name = str(input("Enter Name : "))
    lower = ''
    upper = ''
    
    for char in name:
        if char.islower():
            lower += char
        else:
            upper += char
    sorted_string = lower + upper
    print(sorted_string)