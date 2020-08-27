[![PyPI](https://img.shields.io/pypi/v/rickandmorty?color=important)](https://pypi.org/project/rickandmorty/)
[![Codecov](https://img.shields.io/codecov/c/github/DogukanBaloglu/rickandmorty?color=brightgreen)](https://github.com/DogukanBaloglu/rickandmorty/actions/runs/226808122)
[![GitHub](https://img.shields.io/github/license/DogukanBaloglu/rickandmorty?color=yellow)](https://github.com/DogukanBaloglu/rickandmorty/blob/master/LICENSE)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/DogukanBaloglu/rickandmorty)  
 RICK AND MORTY CLIENT
=======================
 
  *Python implementation for the Rick and Morty API (https://rickandmortyapi.com/)*    
 All methods return json   
 # Installation: 
  
     pip install rickandmorty
      
 # Usage:
  
 ## Import:  
  
     import rickandmorty 
  
 
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
  
 -  getAll()  : You can access the list of characters . 
   
 -  getSingle(id) : You can get a single character by adding the id.
   
 -  getMultiple(ids) : You can get multiple characters by adding  ids.
   
 -  filter(name,status,species,type,gender) : You can also include filters by including additional query parameters.
   
   
 ***Locations:***

    from rickandmorty import Locations
    
  It includes 4 funtions: 
  -  getAll()  
   
  -  getSingle() 
   
  -  getMultiple()
   
  -  filter()  
  
  
 ***Episodes:***

    from rickandmorty import Episodes
  
   It includes 4 funtions: 
 -  getAll() :  
   
 -  getSingle() 
   
 -  getMultiple()
   
 -  filter()
    
 
  ***For detailed information:***  
  - Visit official API Docs https://rickandmortyapi.com/documentation
