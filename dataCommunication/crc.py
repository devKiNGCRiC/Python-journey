# CRC
data = input("Enter data: ")
gen = input("Enter generator: ")
msg = list(data + '0' * (len(gen) - 1))

for i in range(len(data)):
    if msg[i] == '1':
        for j in range(len(gen)):
            msg[i+j] = str(int(msg[i+j]) ^ int(gen[j]))

crc = ''.join(msg[-(len(gen)-1):])
print("CRC:", crc)
print("Transmitted Data:", data + crc)

# Parity
data = input("Enter data: ")
ones = data.count('1')

even = ones % 2
odd = 1 - even

print("Even Parity:", even)
print("Odd Parity:", odd)


# Hamming Code
d = input("Enter 4 bits: ")
h = [0, 0, 0, int(d[0]), 0, int(d[1]), int(d[2]), int(d[3])]
h[1] = h[3] ^ h[5] ^ h[7]
h[2] = h[3] ^ h[6] ^ h[7]
h[4] = h[5] ^ h[6] ^ h[7]

print("Hamming Code:", ''.join(map(str, h[1:])))

r = input("Enter received code: ")
for i in range(1, 8):
    h[i] = int(r[i-1])

s1 = h[1] ^ h[3] ^ h[5] ^ h[7]
s2 = h[2] ^ h[3] ^ h[6] ^ h[7]
s4 = h[4] ^ h[5] ^ h[6] ^ h[7]
error = s1 + 2*s2 + 4*s4

if error:
    h[error] ^= 1
    print("Error at position:", error)
else:
    print("No error detected")

print("Corrected Code:", ''.join(map(str, h[1:])))