[![PyPI](https://img.shields.io/pypi/v/rickandmorty?color=important)](https://pypi.org/project/rickandmorty/)
[![Codecov](https://img.shields.io/codecov/c/github/DogukanBaloglu/rickandmorty?color=brightgreen)](https://github.com/DogukanBaloglu/rickandmorty/actions/runs/226808122)
[![GitHub](https://img.shields.io/github/license/DogukanBaloglu/rickandmorty?color=yellow)](https://github.com/DogukanBaloglu/rickandmorty/blob/master/LICENSE)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/DogukanBaloglu/rickandmorty)   
![image](https://user-images.githubusercontent.com/48068925/91556224-08e83780-e93b-11ea-9322-bcb81e1bf3a0.png)
RICK AND MORTY CLIENT
=======================
 
  *Python implementation for the Rick and Morty API (https://rickandmortyapi.com/)*      

 # Installation: 
  
     pip install rickandmorty
      
 # Usage:
  
     from rickandmorty import *
  
 
 ## Characters:

    from rickandmorty import Characters  
    
| *Key* | *Description*  | 
|--|--|
| id | The id of the character. There are `671` characters . |
| name | The name of the character. | 
| status | The status of the character (`Alive`, `Dead` or `unknown`). |
| species| The species of the character. |
| type| The type or subspecies of the character. | 
| gender| The gender of the character (`Female`, `Male`, `Genderless` or `unknown`). |  

  ***Functions:***  
  
 -  getAll( )  : You can access the list of characters . 
   
 -  getSingle( id ) : You can get a single character by adding the id.
   
 -  getMultiple( ids ) : You can get multiple characters by adding  ids.
   
 -  filter( name , status , species , type , gender ) : You can include filters by including additional query parameters.
   
   
 ## Locations:

    from rickandmorty import Locations
    
| *Key* | *Description*  | 
|--|--|
| id | The id of the location. There are `108` locations . |
| name | The name of the location. | 
| type| The type of the location. | 
| dimension| The dimension in which the location is located. |  

    
  ***Functions:***  
  
  -  getAll( ) : You can access the list of locations.
   
  -  getSingle( id ) : You can get a single location by adding the id.
   
  -  getMultiple( ids ) : You can get multiple locations by adding ids.
   
  -  filter( name , type , dimension ) : You can include filters by including additional query parameters.
  
  
 ## Episodes:

    from rickandmorty import Episodes


| *Key* | *Description*  | 
|--|--|
| id | The id of the episode. There are `41` episodes. |
| name | The name of the episode. | 
| episode| The code of the episode. |  

  
  ***Functions:***   
  
 -  getAll( ) : You can access the list of episodes.   
   
 -  getSingle( id ) : You can get a single episode by adding the id.
   
 -  getMultiple( ids ) : You can get multiple episodes by adding ids.
   
 -  filter( name , episode ) : You can include filters by including additional query parameters.
    
 
  ### For detailed information:    
  
  Visit official API Docs https://rickandmortyapi.com/documentation
