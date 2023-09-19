from rsa import generate_rsa_keypair, save_public_key_to_file, save_private_key_to_file, load_private_key_from_file, load_public_key_from_file, encrypt_message, decrypt_message
import os
from datetime import datetime

# Generate or load the keys
def generate_rsa_keypair_to_path(public_key_path, private_key_path):
    private_key, public_key = generate_rsa_keypair()
    save_private_key_to_file(private_key, private_key_path)
    save_public_key_to_file(public_key, public_key_path)

def get_rsa_keypair_from_path(public_key_path, private_key_path):
    private_key = load_private_key_from_file(private_key_path)
    public_key = load_public_key_from_file(public_key_path)
    return public_key, private_key

def write_encrypted_datetime_to_license(license_file_path, custom_datetime, public_key):
    # Example: custom_datetime = datetime(2023, 9, 18, 15, 30)  # Replace with your desired date and time

    # Convert the custom datetime to a string
    license_data = custom_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Encrypt the license data using the recipient's public key (server's public key)
    encrypted_license = encrypt_message(license_data, public_key)

    # Save the encrypted license data to a license file
    with open(license_file_path, "wb") as license_file:
        license_file.write(encrypted_license)

    print("Custom license data encrypted and saved to:", license_file_path)

def get_decrypted_datetime_from_license(license_file_path, private_key):
    # Read the encrypted license data from the license file
    with open(license_file_path, "rb") as license_file:
        encrypted_license = license_file.read()

    # Decrypt the encrypted license data using the private key
    decrypted_license_data = decrypt_message(encrypted_license, private_key)

    # Convert the decrypted license data (a string) back into a datetime object
    decrypted_datetime = datetime.strptime(decrypted_license_data, "%Y-%m-%d %H:%M:%S")

    print("Decrypted datetime from license file:", decrypted_datetime)
    return decrypted_datetime