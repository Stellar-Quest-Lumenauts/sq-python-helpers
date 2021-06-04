def submit_pre_auth_transaction(transaction, server):
    print(f"Transaction XDR:\n{transaction}\n")
    response = server.submit_transaction(transaction)
    print(f"Server Response:\n{response}")
