from cryptography.fernet import Fernet
import os

# ======== Generate and Save a Key =========
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# ======== Load the Saved Key =========
def load_key():
    return open("secret.key", "rb").read()

# ======== Encrypt a File =========
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        original = file.read()
    
    encrypted = fernet.encrypt(original)
    
    filename = os.path.basename(file_path)
    with open(f"encrypted_files/{filename}", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

# ======== Decrypt a File =========
def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as enc_file:
        encrypted = enc_file.read()
    
    decrypted = fernet.decrypt(encrypted)
    
    filename = os.path.basename(file_path)
    with open(f"decrypted_files/{filename}", "wb") as dec_file:
        dec_file.write(decrypted)

# ======== Main Function =========
def main():
    if not os.path.exists("secret.key"):
        generate_key()

    key = load_key()

    print("\nWelcome to Secure File Encryption Tool 🔒")
    print("Choose an option:")
    print("1. Encrypt a File")
    print("2. Decrypt a File")
    choice = input("\nEnter choice (1/2): ")

    if choice == "1":
        filename = input("\nEnter the filename to encrypt (inside original_files/): ")
        filepath = f"original_files/{filename}"
        if os.path.exists(filepath):
            encrypt_file(filepath, key)
            print(f"\n✅ File '{filename}' encrypted successfully and saved to 'encrypted_files/'")
        else:
            print("\n❌ File not found!")
    
    elif choice == "2":
        filename = input("\nEnter the filename to decrypt (inside encrypted_files/): ")
        filepath = f"encrypted_files/{filename}"
        if os.path.exists(filepath):
            decrypt_file(filepath, key)
            print(f"\n✅ File '{filename}' decrypted successfully and saved to 'decrypted_files/'")
        else:
            print("\n❌ Encrypted file not found!")
    
    else:
        print("\n❌ Invalid choice!")

if __name__ == "__main__":
    main()
