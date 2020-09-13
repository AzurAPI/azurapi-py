import unittest
from azurlane.azurapi import AzurAPI


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.api = AzurAPI()
        
    def test_get_ship_by_name(self):
        ship = self.api.getShipByName(ship='Enterprise')
        self.assertEqual(ship['id'], '077')

    def test_get_ship_by_id(self):
        ship = self.api.getShipById(sid='077')
        self.assertEqual(ship['names']['en'], 'Enterprise')

    def test_get_ship(self):
        ship_by_name = self.api.getShip(ship='Enterprise')
        self.assertEqual(ship_by_name['id'], '077')

        ship_by_id = self.api.getShip(ship='077')
        self.assertEqual(ship_by_id['names']['en'], 'Enterprise')
        

if __name__ == '__main__':
    unittest.main(failfast=True)