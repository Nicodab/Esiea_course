from ast import List
from typing import Optional
from Crypto.Hash import SHA256

def deriv_password(password: bytes, salt: bytes, counter: int) -> Optional[bytes]:
    '''
        - H0 = SHA256 # || = concaténation et 0 est un entier sur 32-bits en little-endian.
        - Hi = SHA256(Hi-1 || password || salt || i) #i is in little endiant, 32bits
    return the value Hn[0:32] ~= H_{counter-1} --> Ici c'est 32 octets --> on prend que les 
    a la fin on se retrouve avec notre clé AES (par exemple)
    '''

def deriv_master_key(km:bytes) -> List[bytes]:
    print("bla")