from Crypto.Random import random
import sys
import string

def generate_random_password(length: int) -> str:
    if length <= 0:
        print("La longueur du mot de passe doit être supérieure à zéro.")
        return ""

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length)) #choice permet de retourner un elem pris au hasard das une séquence.

    return password

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_password.py <length>")
        sys.exit(1)

    try:
        password_length = int(sys.argv[1])
    except ValueError:
        print("La longueur du mot de passe doit être un entier.")
        sys.exit(1)

    generated_password = generate_random_password(password_length)
    print(f"Mot de passe généré : {generated_password}")
