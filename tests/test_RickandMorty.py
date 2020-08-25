import  unittest

from rickandmorty.character_client import Characters
from rickandmorty.location_client import  Locations
from rickandmorty.episode_client import Episodes


class TestCharacters(unittest.TestCase):
    def test_getAll_work_well(self):
        result=671
        func_result=Characters().getAll()['info']['count']
        self.assertEqual(result,func_result)
    def test_getSingle_unexpected_character_number(self):
        result={'error': 'Character not found'}
        func_result= Characters().getSingle(672)
        self.assertEqual(func_result,result)
    def test_getMultiple_unexpected_character_number(self):
        result=[]
        func_result= Characters().getMultiple(672)
        self.assertEqual(func_result,result)
    def test_filter_absent_input(self):
        result={'error': 'There is nothing here'}
        func_result=Characters().filter('xyz')
        self.assertEqual(func_result,result)

class TestEpisodes(unittest.TestCase):
    def test_getAll_work_well(self):
        result=41
        func_result=Episodes().getAll()['info']['count']
        self.assertEqual(result,func_result)
    def test_getSingle_unexpected_episode_number(self):
        result={'error': 'Episode not found'}
        func_result= Episodes().getSingle(42)
        self.assertEqual(func_result,result)
    def test_getMultiple_unexpected_episode_number(self):
        result=[]
        func_result= Episodes().getMultiple(109)
        self.assertEqual(func_result,result)
    def test_filter_absent_input(self):
        result={'error': 'There is nothing here'}
        func_result=Episodes().filter('xyz')
        self.assertEqual(func_result,result)

class TestLocations(unittest.TestCase):
    def test_getAll_work_well(self):
        result=108
        func_result=Locations().getAll()['info']['count']
        self.assertEqual(result,func_result)
    def test_getSingle_unexpected_location_number(self):
        result={'error': 'Location not found'}
        func_result= Locations().getSingle(109)
        self.assertEqual(func_result,result)
    def test_getMultiple_unexpected_location_number(self):
        result=[]
        func_result= Locations().getMultiple(109)
        self.assertEqual(func_result,result)
    def test_filter_absent_input(self):
        result={'error': 'There is nothing here'}
        func_result=Locations().filter('xyz')
        self.assertEqual(func_result,result)

if __name__=='__main__':
    unittest.main()








