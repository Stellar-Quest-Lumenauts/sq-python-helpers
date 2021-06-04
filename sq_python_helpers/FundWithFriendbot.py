import os
import requests

def fund_using_friendbot(public_key):
    # First, check if the account already exists on the testnet
    check_url = f"https://horizon-testnet.stellar.org/accounts/{public_key}"
    r = requests.get(check_url)
    if r.status_code == 404:
        # Let's fund the thing with some XLM, courtesy of friendbot
        url = 'https://friendbot.stellar.org'
        response = requests.get( url, params={'addr': public_key} )
        response.raise_for_status()
