import requests
from .base import Base

class Characters(Base):

    def getAll(self):
        """
         Args: No arg necessary

         Returns: All character informations in the json
        """
        response = requests.get(self.url+'character/')
        return  response.json()
    def getSingle(self,character_order):
        """
                 Args:

                 Returns:
        """
        response = requests.get(self.url +'character/{}'.format(character_order))
        return response.json()
    def getMultiple(self, *orders):
        """
                 Args:

                 Returns:
        """
        y=list(orders)
        response = requests.get(self.url+'character/{}'.format(y))
        return response.json()
    def filter(self, name='',status='',species='',type='', gender=''):
        """
                 Args:

                 Returns:
        """
        payload ={'name':name , 'status':status , 'species':species , 'type':type ,'gender':gender }
        response = requests.get(self.url+'character', params=payload)
        return response.json()

