from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from typing import Optional
from struct import pack

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
    
    # Exemple d'utilisation
    password = b"toto"
    #salt = get_random_bytes(16) 
    # 128 bits
    salt = b'00000000'
    iteration_count = 8192

    derived_password = derive_pwd(password, salt, iteration_count)

    if derived_password is not None:
        #print(f"Mot de passe dérivé : {repr(derived_password)}")
        print(f"Km (mdp dérivée) : {derived_password.hex()}")
        kc, ki = deriv_master_key(derived_password)
        print(f"Kc : {kc.hex()}")
        print(len(kc))
        print(f"Ki : {ki.hex()}")
    else:
        print("Erreur lors de la dérivation du mot de passe.")
