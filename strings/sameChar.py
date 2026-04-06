s=str(input("Enter a Word : "))
a=str(input("Enter alphabet : "))
count = 0
for i in range(len(s)):
    if s[i] == a:
        count = count+1
print(count)