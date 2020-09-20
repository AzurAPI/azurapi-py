import unittest
from azurapi import AzurApi
from core.exceptions import AzurApiException, UnknownShipException


class TestShip(unittest.TestCase):

    def setUp(self):
        self.api = AzurApi(update_on_init=False)

    def test_get_invalid_ship_by_name(self):
        '''
        Test if error is being raised if the name provided for
        a ship does not exist.
        '''
        self.assertRaises(
            UnknownShipException,
            self.api.get_ship_by_name,
            name='not exist'
        )

    def test_get_ship_by_name(self):
        '''
        Test if getting ship by name is possible and testing
        if it is case-insensitive by having the argument all lower cased.
        '''
        ship = self.api.get_ship_by_name('enterprise')
        self.assertEqual(ship.english_name(), 'Enterprise')
        self.assertEqual(ship.id(), '077')

    def test_get_invalid_ship_by_id(self):
        '''
        Test if error is being raised if the id provided for
        a ship does not exist.
        '''
        self.assertRaises(
            UnknownShipException,
            self.api.get_ship_by_id,
            id='not exist'
        )

    def test_get_ship_by_id(self):
        '''
        Test if getting ship by id is possible
        and returns the correct ship data.
        '''
        ship = self.api.get_ship_by_id('077')
        self.assertEqual(ship.english_name(), 'Enterprise')
        self.assertEqual(ship.id(), '077')

    def test_get_invalid_ship_general(self):
        '''
        Test if get_ship() raises the correct exception if
        ship is not found from provided argument.
        '''
        self.assertRaises(
            UnknownShipException,
            self.api.get_ship,
            ship='not exist'
        )

    def test_get_ship_general(self):
        '''
        Test if get_ship() returns the correct ship by
        providing either name or id of the ship.
        '''
        ship_by_name = self.api.get_ship('enterprise')
        self.assertEqual(ship_by_name.english_name(), 'Enterprise')
        self.assertEqual(ship_by_name.id(), '077')

        ship_by_id = self.api.get_ship_by_id('077')
        self.assertEqual(ship_by_id.english_name(), 'Enterprise')
        self.assertEqual(ship_by_id.id(), '077')
