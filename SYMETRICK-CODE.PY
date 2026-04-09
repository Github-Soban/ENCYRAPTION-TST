from cryptography.fernet import Fernet

# Generate a key (keep this secret!)
key = Fernet.generate_key()
f = Fernet(key)

# Message to encrypt
message = b"Red Base is under attack!"

# Encrypt the message
token = f.encrypt(message)
print("Encrypted Message:", token)

# Decrypt the message
decrypted_message = f.decrypt(token)
print("Decrypted Message:", decrypted_message.decode())
