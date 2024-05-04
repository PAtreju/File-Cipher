from cryptography.fernet import Fernet
import time

class CipherFile:

    def encrypt_file(self, key_path, file_path):
        try:
            with open(key_path, 'r') as file:
                key = file.read()
            fernet = Fernet(key)
        except:
            print("Key file not found, please create one first.")
            return 0

        try:
            with open(file_path, 'rb') as file:
                original = file.read()
            encrypted = fernet.encrypt(original)
            with open(file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
        except:
            print("File not found, please check the path.")
            return 0


    def decrypt_file(self, key_path, file_path):
        try:
            with open(key_path, 'r') as file:
                key = file.read()
            fernet = Fernet(key)
        except:
            print("Key file not found, please create one first.")
            return 0

        try:
            with open(file_path, 'rb') as file:
                encrypted = file.read()
            decrypted = fernet.decrypt(encrypted)

            with open(file_path, 'wb') as decrypted_file:
                decrypted_file.write(decrypted)
        except:
            print("File not found, please check the path.")
            return 0

    def create_key(self):
        key = Fernet.generate_key()
        with open('filekey.key', 'wb') as file:
            file.write(key)

# if __name__ == '__main__':
#     choice = input("Do you want to encrypt or decrypt? (e/d)")
#     if choice == 'e':
#         if_key = input("Input path to the key file: (if none exists press enter) \n")
#         if if_key != '':
#             encrypt_file(if_key)
#         else:
#             key = Fernet.generate_key()
#             with open('filekey.key', 'wb ') as file:
#                 file.write(key)
#             encrypt_file('filekey.key')
#     elif choice == 'd':
#         if_key = input("Input path to the key file: (if none exists press enter) \n")
#         if if_key != '':
#             decrypt_file(if_key)