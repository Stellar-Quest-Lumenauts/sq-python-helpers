from typing import Union
from stellar_sdk import TransactionEnvelope, Server

def submit_hash_transaction(transaction: TransactionEnvelope, hex_hash: Union[bytes, str], server: Server) -> dict:
    transaction.sign_hashx(preimage=hex_hash)
    print(f"Transaction XDR:\n{transaction.to_xdr()}\n")
    response = server.submit_transaction(transaction)
    print(f"Server Response:\n{response}")
    return response
