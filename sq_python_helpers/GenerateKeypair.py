from typing import Tuple
from stellar_sdk import Keypair

def generate_keypair() -> Tuple[str, str, Keypair]:
    """Generate and return key information for a random account.

    Returns:
        A tuple containing the secret key, public key, and keypair object.
    """
    keypair = Keypair.random()
    secret_key = keypair.secret
    public_key = keypair.public_key

    return secret_key, public_key, keypair
