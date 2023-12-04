from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes
from typing import Optional
from Crypto.Cipher import AES
from struct import pack
from Crypto.Util.Padding import pad, unpad
import sys

'''
Entrées:
    - Password in bytes
    - path to input file
    - path ot output file

Sortie:
    - MAC & cypted msg written in output file: (Hi = SHA256(Hi-1 + {password} + salt + i))
'''
def encrypt_then_mac(password: bytes, input_file: str, output_file: str):
    # Dérivation du mdp
    iteration_count = 8192
    salt = get_random_bytes(8)
    derived_password = derive_pwd(password, salt, iteration_count)
    if derived_password is None:
        print("Erreur lors de la dérivation du mot de passe.")
        return

    # Dérivation de Km => Kc et Ki
    kc, ki = deriv_master_key(derived_password)

    # Lecture du fichier d'entrée pour avoir la data à chiffrer
    with open(input_file, 'rb') as file:
        plaintext = file.read()

    # Chiffrer les données (protection et confidentialité)
    # IV
    iv = get_random_bytes(16)
    cipher = AES.new(kc, AES.MODE_CBC, iv) # AES-256-CBC avec la clé Kc
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    # Calculer le MAC => HMAC-SHA-256 (protection en intégrité)
    hmac_input = salt + iv + ciphertext
    hmac = HMAC.new(ki, hmac_input, SHA256)
    hmac_digest = hmac.digest()
    print(len(hmac_digest))

    # Écriture du résultat
    with open(output_file, 'wb') as file:
        print(salt + iv + ciphertext + hmac_digest)
        file.write(salt + iv + ciphertext + hmac_digest)

'''
Entrées:
    - Password in bytes
    - path to input file
    - path ot output file

Sortie:
    - information written in output file: (Hi = SHA256(Hi-1 + {password} + salt + i))
'''
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
        print("Usage: python3 protect_symmetric.py <password> <input_file> <output_file>")
        sys.exit(1)

    password = sys.argv[1].encode('utf-8')
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    # SALT : 8 octets
    # IV taille d'un bloc AES -> 128 bits
    #salt = b'00000000' # 8 octets
    
    encrypt_then_mac(password, input_file, output_file)#, salt)
