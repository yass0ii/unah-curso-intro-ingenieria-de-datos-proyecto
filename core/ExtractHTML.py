import requests
from bs4 import BeautifulSoup

class ExtractHTML:
    
    def __init__(self, url: str):
        self.url = url
        
    def get_info_by_contrie(self, countrie: str) -> str:
        """
            Obtiene el html por pais
            @author AlexxFuentes
        """
        res = requests.get(f"{self.url}/{countrie}")
        return res.text if res.status_code == 200 else f"Error al obtener el contenido HTML. Status: {res.status_code}"
    
    def get_info_by_class(self, html: str, name_class: str, element: str) -> str:
        """
            obtiene contenido de una documente HTML por el nombre y el elememento (div)
            @author AlexxFuentes
        """
        soup = BeautifulSoup("".join(html), "html.parser") 
        return soup.find(element, class_ = name_class)# div article-content
    
    
    def conver_to_lower(self, word: str) -> str:
        """
            Corta los espacios en blanco de una cadena y la combierte a minusculas
            @author AlexxFuentes
        """
        return word.strip().lower()
    
    def format_country_name(self, countrie: str) -> str:  
        """
            formatea el nombre de los pa
            @author AlexxFuentes
        """
        if ' ' in countrie:
            n = countrie.split(' ')
            return "-".join(n)
        else:
            return countrie