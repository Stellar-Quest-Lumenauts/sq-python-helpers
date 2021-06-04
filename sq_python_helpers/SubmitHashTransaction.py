def submit_hash_transaction(transaction, hex_hash, server):
    transaction.sign_hashx(preimage=hex_hash)
    print(f"Transaction XDR:\n{transaction.to_xdr()}\n")
    response = server.submit_transaction(transaction)
    print(f"Server Response:\n{response}")
