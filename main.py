from cryptography.fernet import Fernet
import time

def encrypt_file(key_path):
    try:
        with open(key_path, 'r') as file:
            key = file.read()
        fernet = Fernet(key)
    except:
        print("Key file not found, please create one first.")
        time.sleep(10)
        return 0

    file_path = input("Input path to the file you want to encrypt: \n")
    try:
        with open(file_path, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        print("File not found, please check the path.")
        time.sleep(10)
        return 0


def decrypt_file(key_path):
    try:
        with open(key_path, 'r') as file:
            key = file.read()
        fernet = Fernet(key)
    except:
        print("Key file not found, please create one first.")
        time.sleep(10)
        return 0

    file_path = input("Input path to the file you want to decrypt: \n")
    try:
        with open(file_path, 'rb') as file:
            encrypted = file.read()
        decrypted = fernet.decrypt(encrypted)

        with open(file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
    except:
        print("File not found, please check the path.")
        time.sleep(10)
        return 0

if __name__ == '__main__':
    choice = input("Do you want to encrypt or decrypt? (e/d)")
    if choice == 'e':
        if_key = input("Input path to the key file: (if none exists press enter) \n")
        if if_key != '':
            encrypt_file(if_key)
        else:
            key = Fernet.generate_key()
            with open('filekey.key', 'wb ') as file:
                file.write(key)
            encrypt_file('filekey.key')
    elif choice == 'd':
        if_key = input("Input path to the key file: (if none exists press enter) \n")
        if if_key != '':
            decrypt_file(if_key)