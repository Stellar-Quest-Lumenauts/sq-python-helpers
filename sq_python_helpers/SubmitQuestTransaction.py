from stellar_sdk import TransactionEnvelope, Server, Keypair

def submit_quest_transaction(transaction: TransactionEnvelope, keypair: Keypair, server: Server) -> dict:
    """Submit a transaction to the Stellar network.
    
    Args:
        transaction: The transaction envelope to submit to the network.
        keypair: The keypair which should be used to sign the transaction.
        server: The server connection to be used.
    
    Returns:
        The response from the supplied Horizon server.
    """
    transaction.sign(keypair)
    print(f"Transaction XDR:\n{transaction.to_xdr()}\n")
    response = server.submit_transaction(transaction)
    print(f"Server Response:\n{response}")
    return response
