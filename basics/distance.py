import math

x1 = int(input("Enter the value of X1 : "))
y1 = int(input("Enter the value of Y1 : "))
x2 = int(input("Enter the value of X2 : "))
y2 = int(input("Enter the value of Y2 : "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f'Distance Between 2 points : {distance}')