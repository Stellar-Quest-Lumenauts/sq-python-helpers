from stellar_sdk import Keypair

def generate_keypair():
    # Let's make a new keypair to source from
    keypair = Keypair.random()
    secret_key = keypair.secret
    public_key = keypair.public_key

    return secret_key, public_key, keypair
