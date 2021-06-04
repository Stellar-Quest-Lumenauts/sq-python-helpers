from stellar_sdk import TransactionEnvelope, Server

def submit_pre_auth_transaction(transaction: TransactionEnvelope, server: Server) -> dict:
    print(f"Transaction XDR:\n{transaction}\n")
    response = server.submit_transaction(transaction)
    print(f"Server Response:\n{response}")
    return response
