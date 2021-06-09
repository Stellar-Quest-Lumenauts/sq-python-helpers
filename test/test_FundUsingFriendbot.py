"""
Test module sq_python_helpers.FundUsingFriendbot
"""
import json
import requests
import requests_mock
from unittest import TestCase
from stellar_sdk import Keypair, Server, Network, Account

from sq_python_helpers.FundUsingFriendbot import fund_using_friendbot

class FundUsingFriendbotTestCase(TestCase):
    def setUp(self) -> None:
        with open("test/fixtures/funded_account.json", "r") as fixture_file:
            self.funded_account = json.load(fixture_file)
        with open("test/fixtures/unfunded_account.json", "r") as fixture_file:
            self.unfunded_account = json.load(fixture_file)
        with open("test/fixtures/friendbot_successful.json", "r") as fixture_file:
            self.friendbot_successful = json.load(fixture_file)
        self.k = Keypair.random()

    @requests_mock.Mocker()
    def test_account_already_exists(self, m: requests_mock.Mocker):
        m.get(f"https://horizon-testnet.stellar.org/accounts/{self.k.public_key}",
              json=self.funded_account)
        r = fund_using_friendbot(self.k.public_key)
        self.assertIsInstance(r, requests.Response,
                              "item returned is not a response object")
        self.assertIsNotNone(r.json()["account_id"],
                             "response is missing 'account_id'")
        self.assertGreaterEqual(float(r.json()["balances"][0]["balance"]), 1,
                                "native balance is less than 1")


    @requests_mock.Mocker()
    def test_account_not_funded(self, m: requests_mock.Mocker):
        m.get(f"https://horizon-testnet.stellar.org/accounts/{self.k.public_key}",
              json=self.unfunded_account, status_code=404)
        m.get(f"https://friendbot.stellar.org/?addr={self.k.public_key}",
              json=self.friendbot_successful)
        r = fund_using_friendbot(self.k.public_key)
        self.assertIsInstance(r, requests.Response,
                              "item returned is not a response object")
        self.assertTrue(r.json()["successful"],
                        "funding transaction was unsuccessful")
