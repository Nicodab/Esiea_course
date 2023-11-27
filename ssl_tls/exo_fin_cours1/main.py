# le but est de sortir l'empreinte hexadécimal d'un fichier python
# python3 ./main.py ./test.py
# A retenir 3 étapes dans une f° de hashage: new, puis des update par chun de 512 octets par exemple, puis digest
from typing import Optional
from Crypto.Hash import SHA256
import sys
import binascii

# Exemple d'utilisation
#hash_object = SHA256.new()
#hash_object.update(b'mssis2324') # meme résultat que si on faisait 2 lignes séparées hash_object.update(b'mssis') puis hash_object.update(b'2324') avant de faire le digest() et donc avant de fermer la parenthèse.
#print(hash_object.digest())
# on peut faire un pip install cryptodome --user pr éviter de faire un venv


def sha256sum_file(filename: str, chunk_sz=512) -> Optional[bytes]:
    sha256_hash = SHA256.new()
    try:
        with open(filename, "rb") as file:
            data = file.read(chunk_sz)
            while len(data) > 0: # ou alors while(data) ça peut marcher
                sha256_hash.update(data)
                data = file.read(chunk_sz)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    
    return sha256_hash.digest()

if __name__ == '__main__':
    print(len(sys.argv))
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <filename>")
        sys.exit(1)
    #else
    digest = sha256sum_file(sys.argv[1])
    if digest is not None:
        print(binascii.hexlify(digest).decode())
    else:
        print(f"error")
    sys.exit(0)