import re
import json
import os

class Tools:
    """
        @author Kenneth Cruz
        @date 2023-06-20
        @version 0.0.1
        @source 2023-06-12
        
        @modify by AlexxFuentes
    """
    
    def __init__(self):
        pass
    
    
    def readFile(self, path:str, name:str) -> list:
        """
            Lectura de un documento a partir de su ruta.
        """
        f = open(f"{path}/{name}", mode="r")
        data = f.readlines()
        f.close()
        
        return data
    
    
    def saveFile(self, path:str, name:str, data:dict)-> None:
        """
            Guarda un documento dado la ruta y el nombre junto con la extemsion del archivo.
        """
        f = open(f"{path}/{name}", mode="w")
        f.write(data)
        f.close()
        print("Guardado con exito")
        
        
    def saveFileJson(self, path:str, name:str, data:dict)-> None:
        """
            Guarda un documento tipo .json dado la ruta y el nombre junto con la extemsion del archivo.
        """
        with open(f"{path}/{name}", "w") as file:
            json.dump(data, file)
        print("Guardado con exito")
        
    def readFileJson(self, path:str, name:str) -> list:
        """
            Lectura de un documento .json a partir de su ruta.
        """
        with open(f"{path}/{name}", "r") as archivo:
            data = json.load(archivo)
        
        return data
    
    def conver_to_lower(self, word: str) -> str:
        """
            Corta los espacios en blanco de una cadena y la combierte a minusculas
            @author AlexxFuentes
        """
        return word.strip().lower()