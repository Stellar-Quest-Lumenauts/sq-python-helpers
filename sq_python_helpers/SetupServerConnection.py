from stellar_sdk import Server, Network, Account

def setup_server_connection(public_key: str, testnet: bool=True) -> tuple[Server, Account, str, int]:
    """Return connection details in preparation for a transaction.
    
    Args:
        public_key: The source account for the transaction.
        testnet (optional): Whether to use testnet or mainnet. Defaults to True.
    
    Returns:
        A tuple containing the Server object, Account object, network passphrase,
            and the current base fee for the server.
    """
    if testnet:
        server = Server("https://horizon-testnet.stellar.org")
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE
    else:
        server = Server("https://horizon.stellar.org")
        network_passphrase=Network.PUBLIC_NETWORK_PASSPHRASE
    base_fee = server.fetch_base_fee()
    account = server.load_account(public_key)
    return server, account, network_passphrase, base_fee
