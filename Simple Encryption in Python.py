def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        elif char.isdigit():
            shifted_char = str((int(char) + shift) % 10)
        else:
            shifted_char = char
        result += shifted_char
    return result

# Example Usage
message = "Attack at dawn!"
key = 3
encrypted_message = caesar_cipher(message, key)
decrypted_message = caesar_cipher(encrypted_message, -key)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
