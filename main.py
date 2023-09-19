from license import generate_rsa_keypair_to_path, get_rsa_keypair_from_path, write_encrypted_datetime_to_license, get_decrypted_datetime_from_license
from datetime import datetime, timedelta
import time

# Paths for files
public_key_path = "public_key.pem"
private_key_path = "private_key.pem"
license_file_path = "license"

limited_time = datetime.now() + timedelta(seconds=5)

# If there is no key pair files
# generate_rsa_keypair_to_path(public_key_path, private_key_path)

# If there is key pair files
public_key, private_key = get_rsa_keypair_from_path(public_key_path, private_key_path)

# Create or update lisence if you want
write_encrypted_datetime_to_license(license_file_path, limited_time, public_key)

# Load time limit from lisence file
loaded_limit_time = get_decrypted_datetime_from_license(license_file_path, private_key)
print("Expired date: ", loaded_limit_time)

# Program to executed in the time limit
while datetime.now() < loaded_limit_time:
    current_datetime = datetime.now()
    print("Current Datetime:", current_datetime)
    time.sleep(1)  # Sleep for 1 second before printing the next datetime

print("License has expired.")

