height = int(input("Enter the Height of the Triangle : "))
for i in range(height):
        for j in range(height,i,-1):
            print("*" ,  end="")
        print()