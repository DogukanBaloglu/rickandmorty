import requests
from .base import Base

class Locations(Base):
    def getAll(self):
        """
                 Args: No arg necessary

                 Returns: All location informations in the json
        """
        response = requests.get(self.url+'location/')
        return response.json()
    def getSingle(self, location_order):
        response = requests.get(self.url+'location/{}'.format(location_order))
        return response.json()
    def getMultiple(self, *orders):
        y = list(orders)
        response = requests.get(self.url+'location/{}'.format(y))
        return response.json()
    def filter(self, name = '', type='', dimension =''):
        payload = {'name': name ,  'type': type, 'dimension': dimension}
        response = requests.get(self.url+'location/', params=payload)
        return response.json()
