from stellar_sdk import Server, Network, Account

def setup_server_connection(public_key: str, testnet: bool=True) -> tuple[Server, Account, str, int]:
    if testnet:
        server = Server("https://horizon-testnet.stellar.org")
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE
    else:
        server = Server("https://horizon.stellar.org")
        network_passphrase=Network.PUBLIC_NETWORK_PASSPHRASE
    base_fee = server.fetch_base_fee()
    account = server.load_account(public_key)
    return server, account, network_passphrase, base_fee
