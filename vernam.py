def cipher(message: str, key: str) -> str:
    """Encrypt or decrypt a message using the Vernam cipher with a given key.

    Args:
    - message: The message to encrypt or decrypt, as a string of binary data.
    - key: The key to use for encryption or decryption, as a string of binary data.

    Returns:
    - The encrypted or decrypted message, as a string of binary data.
    """
    # Ensure the message and key are of the same length
    if len(message) != len(key):
        raise ValueError("Message and key must be of the same length.")

    # Convert the strings to lists of integers (0 and 1)
    message_bits = [int(bit) for bit in message]
    key_bits = [int(bit) for bit in key]

    # Perform the XOR operation between each bit of the message and the key
    cipher_bits = [str(message_bit ^ key_bit) for message_bit, key_bit in zip(message_bits, key_bits)]

    # Convert the list of bits back to a string
    cipher_text = ''.join(cipher_bits)

    return cipher_text
'''
# Example usage
message = "10101010"  # Example binary message
key = "11001100"     # Example binary key of the same length as the message

encrypted = vernam_cipher(message, key)
print(f"Encrypted: {encrypted}")

# Decrypting the message by applying the same function with the encrypted message and the same key
decrypted = vernam_cipher(encrypted, key)
print(f"Decrypted: {decrypted}")
'''
