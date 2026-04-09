def encrypt_with_key(message, key):
    encrypted_message = ""
    key_length = len(key)
    for i, char in enumerate(message):
        key_char = key[i % key_length]
        encrypted_char = chr(ord(char) + ord(key_char))
        encrypted_message += encrypted_char
    return encrypted_message

def decrypt_with_key(encrypted_message, key):
    decrypted_message = ""
    key_length = len(key)
    for i, char in enumerate(encrypted_message):
        key_char = key[i % key_length]
        decrypted_char = chr(ord(char) - ord(key_char))
        decrypted_message += decrypted_char
    return decrypted_message

message = "AttackAtDawn"
key = "secret"

encrypted_message = encrypt_with_key(message, key)
decrypted_message = decrypt_with_key(encrypted_message, key)

print("Original Message: " + message)
print("Encrypted Message: " + encrypted_message)
print("Decrypted Message: " + decrypted_message)
