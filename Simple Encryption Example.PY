def encrypt(message, key):
  encrypted_message = ''
  for char in message:
    encrypted_char = chr(ord(char) + key)  # Simple Caesar cipher
    encrypted_message += encrypted_char
  return encrypted_message

def decrypt(encrypted_message, key):
  decrypted_message = ''
  for char in encrypted_message:
    decrypted_char = chr(ord(char) - key)
    decrypted_message += decrypted_char
  return decrypted_message

message = "BlueTeamWins!"
key = 3

encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print("Original: ", message)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)
