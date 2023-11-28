# DECHIFFRER LE CIPHER TEXT CHIFFRÉ avec le protect_symetric.py
from struct import pack
from typing import Optional
from Crypto.Hash import HMAC, SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import sys

def decrypt_then_verify(password: bytes, input_file: str, output_file: str):
    # Lecture du fichier d'entrée
    with open(input_file, 'rb') as file:
        data = file.read()

    # On extrait le salt(8 octets)||iv(16 octets)||ciphertext(le reste à lire)||hmac_digest(256 octets car SHA256)
    salt = data[:8]
    iv = data[8:24]
    ciphertext = data[24:-32]
    hmac_digest = data[-32:]

    # Dérivation du mdp
    iteration_count = 8192
    derived_password = derive_pwd(password, salt, iteration_count)
    if derived_password is None:
        print("Erreur lors de la dérivation du mot de passe.")
        return

    # Dérivation de Km => Kc et Ki
    kc, ki = deriv_master_key(derived_password)

    # Vérification HMAC
    hmac_input = salt + iv + ciphertext
    hmac = HMAC.new(ki, hmac_input, SHA256)
    if hmac.digest() != hmac_digest:
        print("Erreur d'intégrité. HMAC ne correspond pas.")
        return

    # Déchiffrement AES-256-CBC
    cipher = AES.new(kc, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    # Écriture du fichier de sortie
    with open(output_file, 'wb') as file:
        file.write(plaintext)

def derive_pwd(password: bytes, salt: bytes, counter: int) -> Optional[bytes]:
    if counter < 1:
        print("Le compteur doit être supérieur ou égal à 1.")
        return None

    # Initial hash: H0 = SHA256(password + salt + 0)
    hash_result = SHA256.new(password + salt + (0).to_bytes(4, 'little')).digest()

    for _ in range(1,counter):
        # Hi = SHA256(Hi-1 + {password} + salt + i)
        hash_result = SHA256.new(hash_result + password + salt + _.to_bytes(4, 'little')).digest()

    return hash_result

def deriv_master_key(km: bytes):
    sha256_ctx = SHA256.new()
    sha256_ctx.update(km)
    sha256_ctx.update(pack("<B", 0))
    kc = sha256_ctx.digest()

    sha256_ctx = SHA256.new()
    sha256_ctx.update(km)
    sha256_ctx.update(pack("<B", 1))
    ki = sha256_ctx.digest()

    return kc, ki

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 unprotect_symetric.py <password> <input_file> <output_file>")
        sys.exit(1)

    password = sys.argv[1].encode('utf-8')
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    decrypt_then_verify(password, input_file, output_file)
