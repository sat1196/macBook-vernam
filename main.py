import sys
import trng as trng
import vernam as vernam

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <message>")
        sys.exit(1)

    message = sys.argv[1]  # Read the message from command line arguments
    message_in_binary = ''.join(format(ord(x), '08b') for x in message)

    key = trng.generate_noise(len(message_in_binary))
    encrypted = vernam.cipher(message_in_binary, key)
    decrypted = vernam.cipher(encrypted, key)

    print(f"Original Message: {message}")
    print(f"Encrypted: {encrypted}")
    decrypted_message = ''.join([chr(int(decrypted[i:i+8], 2)) for i in range(0, len(decrypted), 8)])
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
