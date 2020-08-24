import  unittest

from RickandMorty.character_client import Characters
from RickandMorty.location_client import  Locations
from RickandMorty.episode_client import Episodes


class TestCharacters(unittest.TestCase):
    def test_getSingle_unexpected_character_number(self):
        result={'error': 'Character not found'}
        func_result= Characters().getSingle(672)
        self.assertEqual(func_result,result)
    def test_filter_absent_input(self):
        result={'error': 'There is nothing here'}
        func_result=Characters().filter('xyz')
        self.assertEqual(func_result,result)

class TestEpisodes(unittest.TestCase):
    def test_getSingle_unexpected_episode_number(self):
        result={'error': 'Episode not found'}
        func_result= Episodes().getSingle(42)
        self.assertEqual(func_result,result)
    def test_filter_absent_input(self):
        result={'error': 'There is nothing here'}
        func_result=Episodes().filter('xyz')
        self.assertEqual(func_result,result)

class TestLocations(unittest.TestCase):
    def test_getSingle_unexpected_location_number(self):
        result={'error': 'Location not found'}
        func_result= Locations().getSingle(109)
        self.assertEqual(func_result,result)
    def test_filter_absent_input(self):
        result={'error': 'There is nothing here'}
        func_result=Locations().filter('xyz')
        self.assertEqual(func_result,result)

if __name__=='__main__':
    unittest.main()








