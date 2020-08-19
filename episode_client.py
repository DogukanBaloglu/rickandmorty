import requests
from base import  Base

class Episodes(Base):
    def getAll(self):
        response = requests.get(self.url+'episode/')
        return response.json()
    def getSingle(self, episode):
        response = requests.get(self.url+'episode/{}'.format(episode))
        return response.json()
    def getMultiple(self, *episodes):
        y = list(episodes)
        response = requests.get(self.url+'episode/{}'.format(y))
        return response.json()
    def filter(self , name='', episode=''):
        payload = {'name': name, 'episode': episode}
        response = requests.get(self.url+'episode/', params=payload)
        return response.json()