import requests
from RickandMorty.base  import Base

class Locations(Base):
    def getAll(self):
        """
            Args: No arg necessary

            Returns: All location information in the json
        """
        response = requests.get(self.url+'location/')
        return response.json()
    def getSingle(self, location_order):
        """
            Args: Only one  int value between 1-108.

            Returns: The properties of the given number's defined location.
        """
        response = requests.get(self.url+'location/{}'.format(location_order))
        return response.json()
    def getMultiple(self, *orders):
        """
            Args: int values between 1-108

            Returns: The properties of the given numbers' defined locations.
        """
        y = list(orders)
        response = requests.get(self.url+'location/{}'.format(y))
        return response.json()
    def filter(self, name = '', type='', dimension =''):
        """
            Args: name =filter by the given name.\n
            type=filter by the given type.\n
            dimension=filter by the given dimension.\n

            Returns: Location matching the given values.
        """
        payload = {'name': name ,  'type': type, 'dimension': dimension}
        response = requests.get(self.url+'location/', params=payload)
        return response.json()
