# Error Detection and Correction 
# 1. Parity Check 
# 2. CRC 
# 3. Hamming Code 
def parity_check(): 
    data = input("Enter binary data: ") 
    ones = data.count('1') 
    if ones % 2 == 0: 
        parity = '0' 
    else: 
        parity = '1' 
    transmitted = data + parity 
    print("\nEven Parity Bit :", parity) 
    print("Transmitted Data :", transmitted) 

def xor(a, b): 
    result = "" 
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result += "0" 
        else: 
            result += "1" 
    return result 

def crc():
    data = input("Enter binary data: ")
    divisor = input("Enter generator polynomial: ")
    dividend = data + "0" * (len(divisor) - 1)
    tmp = dividend[:len(divisor)]
    i = len(divisor)
    while i < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp)
        else:
            tmp = xor('0' * len(divisor), tmp)
        tmp += dividend[i]
        i += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * len(divisor), tmp)
    remainder = tmp

    print("\nCRC Remainder :", remainder)
    print("Transmitted Data :", data + remainder)

def hamming(): 
    data = input("Enter 4-bit binary data: ") 
    d1 = int(data[0]) 
    d2 = int(data[1]) 
    d3 = int(data[2]) 
    d4 = int(data[3]) 
    p1 = d1 ^ d2 ^ d4 
    p2 = d1 ^ d3 ^ d4 
    p4 = d2 ^ d3 ^ d4 
    code = str(p1) + str(p2) + str(d1) + str(p4) + str(d2) + str(d3) + str(d4) 
    print("\nHamming Code :", code) 

while True: 
    print("\n------ MENU ------") 
    print("1. Parity Check") 
    print("2. CRC") 
    print("3. Hamming Code") 
    print("4. Exit") 
    choice = int(input("Enter your choice: ")) 
    if choice == 1: 
        parity_check() 
    elif choice == 2: 
        crc() 
    elif choice == 3: 
        hamming() 
    elif choice == 4: 
        print("Program Ended") 
        break 
    else: 
        print("Invalid Choice")