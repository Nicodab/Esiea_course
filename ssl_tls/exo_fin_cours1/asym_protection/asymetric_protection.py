# Exercice: Faire un peu pareil mais avec une protection asymmétrique:
# Un peu le même principe que précdemment mais en faisant un chiffrement de message AES pour avoir le chiffré
# Donc 1ere étape: chiffrer le message avec AES-256-CBC en générant un Kc avec une fonction de Crypto.Random et aussi à l'aide d'un iv généré aléatoirement 
# Ensuite 2ème étape: Faire du RSA: Donc fil faut faire de la séquestration de clé (à partir du Kc de chiffrement) à l'aide de de la clé publique du destinataire 
# Une fois qu'on a utilisé RSA_OAEP avec en entrée la clé Kc et la clé publique du destinataire on se retrouve avec le séquestre
# Enfin Etape 3: On utilise le séquestre généré précédemment pour signer le message.
# Le message est signé avec la concaténation de la clé de séquestre "Seq", l'IV et le chiffré --> Seq||IV||C. Et donc avec cette entrée, on va signer cette dernière avec une clé privée à l'aide de RSA-PSS
# Finalement on va stocker dans un fichier de sortie la concaténation de  Seq||IV||C||S, S étant la sortie de la signature.
# Et donc voilà pour le fonctionnement du programme, on prend un fichier d'entrée .txt dans lequel y'a le message ainsi qu'un fichier de sorti dans lequel on écrira la sortie de notre programme
import sys
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from typing import Optional
from struct import pack
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
# Pour séquestrer la clé
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
# Pour la signature
from Crypto.Signature import pss

def encrypt_AES_and_wrap_key(input_file: str):
    # Lecture du fichier d'entrée pour avoir la data à chiffrer
    with open(input_file, 'rb') as file:
        plaintext = file.read()
        
    # Chiffrer les données (protection et confidentialité)
     # Génération de kc et iv pour le chiffrtement AES
    kc = get_random_bytes(32) # Kc aléatoire
    iv = get_random_bytes(16) # IV aléatoire (taille iv = taille d'un bloc d'aes 256)
    cipher = AES.new(kc, AES.MODE_CBC, iv) # AES-256-CBC avec la clé Kc
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    # Séquestration de la clé
    public_dest_key = RSA.importKey(open('preceiver.pem').read())
    cipher_public_dest_key = PKCS1_OAEP.new(public_dest_key)
    cipher_seq_text = cipher_public_dest_key.encrypt(kc) # ON CHIFFRE kc à l'aide de la clé publique du destinataire et pas le msg

    # Signature de l'entrée "Seq||IV||C"
    seq_iv_c = cipher_seq_text + iv + ciphertext
    h = SHA256.new(seq_iv_c)
    private_key = RSA.import_key(open('private.pem').read())
    signature = pss.new(private_key).sign(h)

    print(seq_iv_c + signature)
    # Écriture du résultat dans le fichier de sortie
    with open(output_file, 'wb') as file:
        file.write(seq_iv_c + signature)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 unprotect_symetric.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    encrypt_AES_and_wrap_key(input_file)
