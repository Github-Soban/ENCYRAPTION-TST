from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Generate private key (keep this SECRET!)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=512
)

#Get public key from private key
public_key = private_key.public_key()

# Message to encrypt
message = b"Blue Base has the flag!"

#Encrypt the message using public key
encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Encrypted Message:", encrypted)

#Decrypt the message using private key
decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Decrypted Message:", decrypted.decode())
