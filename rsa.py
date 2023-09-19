from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_rsa_keypair(key_size=2048):
    """
    Generate an RSA key pair.

    Args:
        key_size (int): The size of the key (e.g., 2048, 3072).

    Returns:
        tuple: A tuple containing the private key and the public key.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
    )
    public_key = private_key.public_key()

    return private_key, public_key

def save_private_key_to_file(private_key, filename):
    """
    Save an RSA private key to a file.

    Args:
        private_key: The RSA private key to save.
        filename (str): The name of the file to save the private key to.
    """
    with open(filename, "wb") as key_file:
        key_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        key_file.write(key_pem)

def save_public_key_to_file(public_key, filename):
    """
    Save an RSA public key to a file.

    Args:
        public_key: The RSA public key to save.
        filename (str): The name of the file to save the public key to.
    """
    with open(filename, "wb") as key_file:
        key_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        key_file.write(key_pem)

def load_private_key_from_file(filename):
    """
    Load an RSA private key from a file.

    Args:
        filename (str): The name of the file containing the private key.

    Returns:
        private_key: The loaded RSA private key.
    """
    with open(filename, "rb") as key_file:
        key_pem = key_file.read()
        private_key = serialization.load_pem_private_key(
            key_pem,
            password=None
        )
    return private_key

def load_public_key_from_file(filename):
    """
    Load an RSA public key from a file.

    Args:
        filename (str): The name of the file containing the public key.

    Returns:
        public_key: The loaded RSA public key.
    """
    with open(filename, "rb") as key_file:
        key_pem = key_file.read()
        public_key = serialization.load_pem_public_key(key_pem)
    return public_key

def encrypt_message(message, recipient_public_key):
    """
    Encrypt a message using RSA.

    Args:
        message (str): The message to encrypt.
        recipient_public_key: The recipient's public key.

    Returns:
        bytes: The encrypted message.
    """
    encrypted_message = recipient_public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_message

def decrypt_message(encrypted_message, private_key):
    """
    Decrypt an encrypted message using RSA.

    Args:
        encrypted_message: The encrypted message.
        private_key: The recipient's private key.

    Returns:
        str: The decrypted message.
    """
    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).decode()
    return decrypted_message
