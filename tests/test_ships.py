import unittest
from azurapi import AzurApi
from core.exceptions import AzurApiException, UnknownShipException


class TestShip(unittest.TestCase):

    def setUp(self):
        self.api = AzurApi()

    def test_get_invalid_ship(self):
        '''
        Test if error is being raised if the name provided for
        a ship does not exist
        '''
        self.assertRaises(
            UnknownShipException,
            self.api.get_ship_by_name,
            name='not exist'
        )

    def test_get_ship_by_name(self):
        '''
        This tests if getting ship by name is possible and testing
        if it is case-insensitive by having the argument all lower cased.
        '''
        ship = self.api.get_ship_by_name('enterprise')
        self.assertEqual(ship.get_english_name(), 'Enterprise')
        self.assertEqual(ship.get_id(), '077')
