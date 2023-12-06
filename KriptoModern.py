def generate_key_bits(message, key):
    key_bits = ""
    key_len = len(key)
    message_len = len(message)

    for i in range(message_len):
        key_bits += format(ord(key[i % key_len]), '08b')

    return key_bits[:message_len]

def vigenere_encrypt_bits(message, key):
    encrypted_bits = ""
    key_bits = generate_key_bits(message, key)

    for i in range(len(message)):
        if message[i] != ' ':
            encrypted_bits += str(int(message[i]) ^ int(key_bits[i]))

    return encrypted_bits

def vigenere_decrypt_bits(ciphertext_bits, key):
    decrypted_message = ""
    key_bits = generate_key_bits(ciphertext_bits, key)

    for i in range(0, len(ciphertext_bits), 8):
        block = ciphertext_bits[i:i+8]
        decrypted_block = ''.join([str(int(block[j]) ^ int(key_bits[i+j])) for j in range(8)])
        decrypted_message += chr(int(decrypted_block, 2))

    return decrypted_message

# Input pesan dan kunci dari pengguna
pesan = input("Masukkan pesan: ")
kunci = input("Masukkan kunci: ")

# Menampilkan pesan dan kunci dalam bentuk bit
pesan_bits = ''.join(format(ord(char), '08b') for char in pesan)
kunci_bits = ''.join(format(ord(char), '08b') for char in kunci)
print("Pesan dalam bentuk bit:", pesan_bits)
print("Kunci dalam bentuk bit:", kunci_bits)

# Enkripsi
encrypted_bits = vigenere_encrypt_bits(pesan_bits, kunci)
print("Pesan yang dienkripsi :", encrypted_bits)

# Dekripsi
decrypted_message = vigenere_decrypt_bits(encrypted_bits, kunci)
print("Pesan yang didekripsi:", decrypted_message)
