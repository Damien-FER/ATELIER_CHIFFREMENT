import os
from pathlib import Path
import nacl.secret
import nacl.utils

def get_box():
    # SecretBox nécessite une clé de 32 octets exactement
    key_hex = os.environ.get("NAC_KEY_HEX")
    if not key_hex:
        # On génère une clé compatible si absente
        new_key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
        raise SystemExit(f"❌ NAC_KEY_HEX non défini.\n"
                         f"Génère une clé avec: python3 -c \"import nacl.utils; print(nacl.utils.random(32).hex())\"\n"
                         f"Puis fait: export NAC_KEY_HEX='ta_cle_hex'")
    
    return nacl.secret.SecretBox(bytes.fromhex(key_hex))

def main():
    box = get_box()
    
    # 1. Message à protéger
    message = b"Ceci est un secret chiffre avec PyNaCl SecretBox"
    
    # 2. Chiffrement (PyNaCl gère le nonce automatiquement)
    encrypted = box.encrypt(message)
    print("✅ Message chiffré (hex) :", encrypted.hex())

    # 3. Déchiffrement
    try:
        decrypted = box.decrypt(encrypted)
        print("✅ Message déchiffré :", decrypted.decode())
    except Exception:
        print("❌ Erreur : Clé invalide ou message altéré !")

if __name__ == "__main__":
    main()