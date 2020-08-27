[![PyPI](https://img.shields.io/pypi/v/rickandmorty?color=important)](https://pypi.org/project/rickandmorty/)
[![Codecov](https://img.shields.io/codecov/c/github/DogukanBaloglu/rickandmorty?color=brightgreen)](https://github.com/DogukanBaloglu/rickandmorty/actions/runs/226808122)
[![GitHub](https://img.shields.io/github/license/DogukanBaloglu/rickandmorty?color=yellow)](https://github.com/DogukanBaloglu/rickandmorty/blob/master/LICENSE)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/DogukanBaloglu/rickandmorty)  
 Rick And Morty Client 
=======================
 
  *Python implementation for the Rick and Morty API (https://rickandmortyapi.com/)*    
 All methods return json   
 ## Installation: 
  
     pip install rickandmorty
      
 ## Usage:
  
  ***Import:***  
  
     import rickandmorty 
  
 
 ***Characters:***

    from rickandmorty import Characters
    
  
 ***Locations:***

    from rickandmorty import Locations
    

 ***Episodes:***

    from rickandmorty import Episodes
    
    
 
  
   - It includes 4 funtions:  
  1.getAll(): Returns, all characters information.    
  2.getSingle(): Returns, the properties of the given number's defined character (Between 1 to 671).        
  3.getMultiple(): Returns, The properties of the given numbers' defined characters (Between 1 to 671).        
  4.filter(): Returns,Characters matching the given values(name,status,species,type,gender).  
  
   - It includes 4 funtions:  
  1.getAll(): Returns, all locations information.      
  2.getSingle(): Returns, the properties of the given number's defined location (Between 1 to 108).          
  3.getMultiple(): Returns, The properties of the given numbers' defined locations (Between 1 to 108).          
  4.filter(): Returns,Locations matching the given values(name,type,dimension).  
  
   - It includes 4 funtions:  
  1.getAll(): Returns, all episodes information.    
  2.getSingle(): Returns, the properties of the given number's defined episode (Between 1 to 42).        
  3.getMultiple(): Returns, The properties of the given numbers' defined episodes (Between 1 to 42).        
  4.filter(): Returns,Episodes matching the given values(name,episode). 
  
  ***For detailed information:***  
  - Visit official API Docs https://rickandmortyapi.com/documentation
