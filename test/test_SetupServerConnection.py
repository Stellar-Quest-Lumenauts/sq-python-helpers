"""
Test module sq_python_helpers.SetupServerConnection
"""
import json
import requests
import requests_mock
from unittest import TestCase
from stellar_sdk import Keypair, Server, Network, Account

from sq_python_helpers.SetupServerConnection import setup_server_connection

class SetupServerConnectionTestCase(TestCase):
    @requests_mock.Mocker()
    def setUp(self, m: requests_mock.Mocker) -> None:
        with open("test/fixtures/funded_account.json", "r") as fixture_file:
            self.funded_account = json.load(fixture_file)
            self.account_id = self.funded_account.get("account_id")
        with open("test/fixtures/testnet_ledger.json", "r") as fixture_file:
            self.ledger = json.load(fixture_file)
        m.get("https://horizon-testnet.stellar.org/ledgers?order=desc&limit=1",
              json=self.ledger)
        m.get("https://horizon.stellar.org/ledgers?order=desc&limit=1",
              json=self.ledger)
        m.get(f"https://horizon-testnet.stellar.org/accounts/{self.account_id}",
              json=self.funded_account)
        m.get(f"https://horizon.stellar.org/accounts/{self.account_id}",
              json=self.funded_account)
        self.testnet_conn = setup_server_connection(self.account_id)
        self.mainnet_conn = setup_server_connection(self.account_id, testnet=False)

    def test_return_four_items(self):
        self.assertEqual(len(self.testnet_conn), 4,
                         'wrong number of items returned')
        self.assertEqual(len(self.mainnet_conn), 4,
                         'wrong number of items returned')

    def test_return_expected_types(self):
        self.assertIsInstance(self.testnet_conn[0], Server,
                              'first item is not a Server object')
        self.assertIsInstance(self.mainnet_conn[0], Server,
                              'first item is not a Server object')
        self.assertIsInstance(self.testnet_conn[1], Account,
                              'second item is not an Account object')
        self.assertIsInstance(self.mainnet_conn[1], Account,
                              'second item is not an Account object')
        self.assertIsInstance(self.testnet_conn[2], str,
                              'third item is not a string')
        self.assertIsInstance(self.mainnet_conn[2], str,
                              'third item is not a string')
        self.assertIsInstance(self.testnet_conn[3], int,
                              'fourth item is not an integer')
        self.assertIsInstance(self.mainnet_conn[3], int,
                              'fourth item is not an integer')

    def test_return_main_test_details(self):
        self.assertEqual(self.testnet_conn[0].horizon_url, "https://horizon-testnet.stellar.org",
                         'incorrect horizon_url returned')
        self.assertEqual(self.mainnet_conn[0].horizon_url, "https://horizon.stellar.org",
                         'incorrect horizon_url returned')
        self.assertEqual(self.testnet_conn[2], "Test SDF Network ; September 2015",
                         'incorrect network passphrase returned')
        self.assertEqual(self.mainnet_conn[2], "Public Global Stellar Network ; September 2015",
                         'incorrect network passphrase returned')

    def test_account_sequence_number(self):
        self.assertEqual(self.testnet_conn[1].sequence, 5919212258197504,
                         'incorrect account sequence number returned')
        self.assertEqual(self.mainnet_conn[1].sequence, 5919212258197504,
                         'incorrect account sequence number returned')

    def test_return_base_fee(self):
        self.assertEqual(self.testnet_conn[3], 100,
                         'incorrect base_fee returned')
        self.assertEqual(self.mainnet_conn[3], 100,
                         'incorrect base_fee returned')
