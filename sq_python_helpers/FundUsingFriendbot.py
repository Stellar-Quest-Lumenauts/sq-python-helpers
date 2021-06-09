import requests

def fund_using_friendbot(public_key: str) -> requests.Response:
    """Use friendbot to ensure a testnet account exists and is funded.

    Args:
        public_key: The public key to test, and fund if necessary.

    Returns:
        HTTP response object from the funding operation.
    """
    check_url = f"https://horizon-testnet.stellar.org/accounts/{public_key}"
    r = requests.get(check_url)
    if r.status_code == 404:
        url = 'https://friendbot.stellar.org'
        response = requests.get( url, params={'addr': public_key} )
        response.raise_for_status()
        return response
    else:
        return r
