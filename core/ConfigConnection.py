import configparser
import os
import re


class ConfigConnection: 
    """
        Obtiene y parsea los datos del archivo de configuración 
        en una estructura de tipo diccionario
        @author kenneth.cruz@unah.hn
        @version 0.1.0
        @date 20023/04/18
        @since 20023/04/18
    """

    def __init__(self, path): 
        self.path = path
        self.parser = configparser.ConfigParser()
        self.parser.read(self.path)

        
    def getConfig(self) -> dict: 
        """
            Toma los valores del archivo de configuración; retorna un diccionario
        """
        config = self.parser["DEFAULT"]
        config = dict(zip(config.keys(), config.values()))
        return config