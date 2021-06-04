from stellar_sdk import Keypair

def load_key_information(secret_key: str) -> tuple[str, str, Keypair]:
    """Return key information for a given secret key.
    
    Args:
        secret_key: The secret key to get key information for.
        
    Returns:
        A tuple containing the secret key, public key, and keypair object.
    """
    keypair = Keypair.from_secret(secret_key)
    public_key = keypair.public_key
    return secret_key, public_key, keypair
