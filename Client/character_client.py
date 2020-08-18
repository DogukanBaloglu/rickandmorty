import requests
from base import Base

class Characters(Base):

    def getAll(self):
        response = requests.get(self.url+'character/')
        return  response.json()
    def getSingle(self,character_order):
        response = requests.get(self.url +'character/{}'.format(character_order))
        return response.json()
    def getMultiple(self, *orders):
        y=list(orders)
        response = requests.get(self.url+'character/{}'.format(y))
        return response.json()
    def filter(self, name='',status='',species='',type='', gender=''):
        payload ={'name':name , 'status':status , 'species':species , 'type':type ,'gender':gender }
        response = requests.get(self.url+'character', params=payload)
        return response.json()

