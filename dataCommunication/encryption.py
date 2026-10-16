from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

message = b"Hello Network Security"

# Symmetric Encryption
key = Fernet.generate_key()
cipher = Fernet(key)

encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)

print("SYMMETRIC ENCRYPTION")
print("Original :", message.decode())
print("Encrypted:", encrypted)
print("Decrypted:", decrypted.decode())

# Asymmetric Encryption - RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nASYMMETRIC ENCRYPTION")
print("Original :", message.decode())
print("Encrypted:", encrypted)
print("Decrypted:", decrypted.decode())
