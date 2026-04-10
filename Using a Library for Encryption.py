from cryptography.fernet import Fernet

# Generate a key (keep this SECRET!)
key = Fernet.generate_key()
f = Fernet(key)

# Encrypt the message
message = b'Red vs Blue'
encrypted = f.encrypt(message)
print(f'Encrypted: {encrypted}')

# Decrypt the message
decrypted = f.decrypt(encrypted)
print(f'Decrypted: {decrypted}')
