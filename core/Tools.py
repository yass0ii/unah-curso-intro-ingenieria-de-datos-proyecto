import re

class Tools:
    """
        @author Kenneth Cruz
        @date 2023-06-20
        @version 0.0.1
        @source 2023-06-12
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