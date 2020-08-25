import requests
from RickandMorty.base  import Base

class Characters(Base):

    def getAll(self):
        """
            Args: No arg necessary

            Returns: All character information in the json format.
        """
        response = requests.get(self.url+'character/')
        return  response.json()
    def getSingle(self,character_order):
        """
            Args: Only one  int value between 1-671

            Returns: The properties of the given number's defined character.
        """
        response = requests.get(self.url +'character/{}'.format(character_order))
        return response.json()
    def getMultiple(self, *orders):
        """
            Args: int values between 1-671

            Returns: The properties of the given numbers' defined characters.
        """
        y=list(orders)
        response = requests.get(self.url+'character/{}'.format(y))
        return response.json()
    def filter(self, name='',status='',species='',type='', gender=''):
        """
            Args: name =filter by the given name.\n
            status=filter by the given status  (alive , dead , unknown),\n
            species=filter by the given species(Human...),\n
            type= filter by the given type,\n
            gender=filter by the given gender(male ,female,genderless,unknown)\n

            Returns: Characters matching the given values.
        """
        payload ={'name':name , 'status':status , 'species':species , 'type':type ,'gender':gender }
        response = requests.get(self.url+'character', params=payload)
        return response.json()

