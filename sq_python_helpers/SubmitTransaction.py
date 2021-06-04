def submit_quest_transaction(transaction, keypair, server):
    transaction.sign(keypair)
    print(f"Transaction XDR:\n{transaction.to_xdr()}\n")
    response = server.submit_transaction(transaction)
    print(f"Server Response:\n{response}")
