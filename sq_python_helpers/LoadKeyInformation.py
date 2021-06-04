from stellar_sdk import Keypair

def load_key_information(secret_key: str) -> tuple[str, str, Keypair]:
    # Take a secret key and return secret, public, and keypair
    keypair = Keypair.from_secret(secret_key)
    public_key = keypair.public_key
    return secret_key, public_key, keypair
