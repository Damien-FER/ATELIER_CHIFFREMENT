import os
from cryptography.fernet import Fernet

def charger_cle():
    # Récupère la clé dans les variables d'environnement (Secret GitHub)
    cle = os.environ.get("MY_FERNET_KEY")
    if not cle:
        raise ValueError("Erreur : La variable MY_FERNET_KEY est absente !")
    return cle.encode()

def main():
    cle = charger_cle()
    f = Fernet(cle)

    # Exemple de chiffrement
    message = "Donnée protégée par Secret GitHub"
    token = f.encrypt(message.encode())
    print(f"Token chiffré : {token.decode()}")

    # Exemple de déchiffrement
    original = f.decrypt(token).decode()
    print(f"Message déchiffré : {original}")

if __name__ == "__main__":
    main()