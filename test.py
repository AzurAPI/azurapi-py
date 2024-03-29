import unittest
from azurlane.azurapi import AzurAPI


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.api = AzurAPI()

    def test_get_all_ships(self):
        '''
        No assertion as this is for general testing
        '''
        self.api.getAllShips()
        
    def test_get_ship_by_name(self):
        ship = self.api.getShipByName(ship='Enterprise')
        self.assertEqual(ship['id'], '077')

    def test_get_ship_by_id(self):
        ship = self.api.getShipById(sid='077')
        self.assertEqual(ship['names']['en'], 'Enterprise')

    def test_get_ship(self):
        '''
        Lowecase for 'enterprise' to test case insensitivity
        '''
        ship_by_name = self.api.getShip(ship='enterprise')
        self.assertEqual(ship_by_name['id'], '077')

        ship_by_id = self.api.getShip(ship='077')
        self.assertEqual(ship_by_id['names']['en'], 'Enterprise')

    def test_get_all_ships_by_lang(self):
        '''
        Test for one language and assume other languages are correct
        No assertion as this is for general testing
        '''
        self.api.getAllShipsByLang('en')

    def test_get_ship_by_lang(self):
        '''
        Test for one language and assume other languages are correct
        This effectively also tests for getShipsBy<Lang>Name
        '''
        ship = self.api.getShipByLang('en', 'Enterprise')
        self.assertEqual(ship['id'], '077')

    def test_get_all_ships_by_faction(self):
        '''
        No assertion as this is for general testing
        '''
        self.api.getAllShipsFromFaction(faction='Sakura Empire')

    def test_get_all_equipment_by_lang(self):
        '''
        No assertion as this is for general testing
        '''
        gun = self.api.getAllEquipmentsByLang('en')

    def test_get_equipment_by_name(self):
        '''
        Test for one language and assume other languages are correct
        '''
        gun = self.api.getEquipmentByEnglishName('Prototype Quadruple 356mm Main Gun Mount MkB')


if __name__ == '__main__':
    unittest.main(failfast=True)
