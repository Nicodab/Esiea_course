import sys
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import pss
from Crypto.Util.Padding import unpad

def decrypt_AES_and_unwrap_key(input_file: str):
    with open(input_file, 'rb') as file:
        data = file.read()

    # Extraction de la séquence, IV, ciphertext et la signature
    seq_len = 256  # La longueur de la clé séquestrée est de 256 bits
    seq = data[:seq_len]
    iv = data[seq_len:seq_len+16]
    ciphertext = data[seq_len+16:-256]
    signature = data[-256:]

    # Déchiffrer la clé séquestrée avec la clé privée
    private_key = RSA.import_key(open('private.pem').read())
    cipher_private_key = PKCS1_OAEP.new(private_key)
    kc = cipher_private_key.decrypt(seq)

    # Vérifier la signature
    h = SHA256.new(seq + iv + ciphertext)
    verifier = pss.new(private_key)
    try:
        verifier.verify(h, signature)
        print("La signature est valide.")
    except (ValueError, TypeError):
        print("La signature est invalide.")

    # Déchiffrer le message avec la clé kc
    cipher = AES.new(kc, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)

    return decrypted_message.decode('utf-8')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 asymetric_unprotection.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    decrypted_message = decrypt_AES_and_unwrap_key(input_file) # une fois que c'est bon on renvoi juste un 0 si c'ets ok et ne pas juste l'écrire dans un fichier texte car sinon ça ne passera pas les test automatiques du prof.

    # Écriture du résultat dans le fichier de sortie
    with open(output_file, 'w') as file:
        file.write(decrypted_message)

    print("Le message a été déchiffré avec succès.")
