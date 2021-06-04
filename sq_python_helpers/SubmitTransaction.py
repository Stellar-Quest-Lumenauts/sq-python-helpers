from stellar_sdk import TransactionEnvelope, Server, Keypair

def submit_quest_transaction(transaction: TransactionEnvelope, keypair: Keypair, server: Server) -> dict:
    transaction.sign(keypair)
    print(f"Transaction XDR:\n{transaction.to_xdr()}\n")
    response = server.submit_transaction(transaction)
    print(f"Server Response:\n{response}")
    return response
