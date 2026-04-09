from cryptography.fernet import Fernet

# Generate a key (keep this secret!)
key = Fernet.generate_key()
f = Fernet(key)

# Our secret message
message = b"The Blue Team will prevail!"

# Encrypt the message
token = f.encrypt(message)

# Decrypt the message
decrypted_message = f.decrypt(token)

print("Original message:", message.decode())
print("Encrypted message:", token)
print("Decrypted message:", decrypted_message.decode())
