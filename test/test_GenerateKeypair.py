"""
Test module sq_python_helpers.GenerateKeypair
"""
from unittest import TestCase
from stellar_sdk import Keypair

from sq_python_helpers.GenerateKeypair import generate_keypair

class GenerateKeypairTestCase(TestCase):
    def setUp(self) -> None:
        self.k = generate_keypair()

    def test_return_three_items(self):
        self.assertEqual(len(self.k), 3,
                         'wrong number of items returned')

    def test_return_expected_types(self):
        self.assertIsInstance(self.k[0], str,
                              'first item is not a string')
        self.assertIsInstance(self.k[1], str,
                              'second item is not a string')
        self.assertIsInstance(self.k[2], Keypair,
                              'third item is not a Keypair object')

    def test_public_secret_keypair_match(self):
        self.assertEqual(self.k[0], self.k[2].secret,
                         'returned secret key does not match returned keypair')
        self.assertEqual(self.k[1], self.k[2].public_key,
                         'returned public key does not match returned keypair')
