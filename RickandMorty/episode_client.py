import requests
from .base import Base

class Episodes(Base):
    def getAll(self):
        """
            Args: No arg necessary

            Returns: All episode information in the json
        """
        response = requests.get(self.url+'episode/')
        return response.json()
    def getSingle(self, episode):
        """
            Args: Only one  int value between 1-42.

            Returns: The properties of the given number's defined episode.
        """
        response = requests.get(self.url+'episode/{}'.format(episode))
        return response.json()
    def getMultiple(self, *episodes):
        """
            Args: int values between 1-42

            Returns: The properties of the given numbers' defined episodes.
        """
        y = list(episodes)
        response = requests.get(self.url+'episode/{}'.format(y))
        return response.json()
    def filter(self , name='', episode=''):
        """
            Args: name =filter by the given name.\n
            episode=filter by the given episode code.\n

            Returns: Episode matching the given values.
        """
        payload = {'name': name, 'episode': episode}
        response = requests.get(self.url+'episode/', params=payload)
        return response.json()