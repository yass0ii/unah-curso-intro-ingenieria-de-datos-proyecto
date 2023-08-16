from bs4 import BeautifulSoup
import re

class ProcessHTML:
    
    def __init__(self):
        pass
    
    def get_divs(self, html: str):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.find_all('div', id=True)
    
    def get_value_h2(self, tag) -> str:
        return tag.find('h2').text.strip() # Valor del <h2>valor</h2>
    
    def get_value_p(self, tag) -> str: 
        return tag.find_next('p').text.strip() # Valor del <p>valor</p>  
    
    def get_alls_h3(self, tag) -> str:
        return tag.find_all('h3')
    
    def parse_p_tags(self, p: str):
        result = {}
        p = str(p)

        soup = BeautifulSoup(p, 'html.parser')
        strong_tags = soup.find_all('strong')

        if len(strong_tags) == 0:
            return soup.get_text()
        else:
            for strong_tag in strong_tags:
                key = strong_tag.get_text()
                sibling = strong_tag.find_next_sibling(string=True)
                if sibling is not None:
                    value = sibling.strip()
                    result[key] = value
    
        return result
        
    def limpiar_campos(self, text: str) -> str:
        result = re.search(r'([\d,.]+)(?:\s*(?:%|sq km|years))?', str(text))

        if result:
            extracted_number = result.group(1)

            if '(' in text and ')' in text:
                return '0'

            if ',' in extracted_number:
                number = extracted_number.replace(',', '')
                return number
            else:
                return extracted_number

        return text

    def limpiar(self, text: str) -> str:
        result = re.search(r'(-?[\d,.]+)\s*m', str(text))

        if result:
            extracted_number = result.group(1)
            if ',' in extracted_number:
                number = extracted_number.replace(',', '')
                return number
            else:
                return result.group(1)

        return text


    def limpiar_porcentaje(self, text: str) -> str:
        result = re.search(r'([\d.]+)%', str(text))

        if result:
            extracted_number = result.group(1)
            return extracted_number

        return text


    def convertir_a_miles_millones(self, numero_str):
        numero_str = numero_str.replace('$', '').replace(' billion', 'e9')
        if ',' in numero_str:
            numero_str = numero_str.replace(',', '')
        else:
            numero_str = numero_str.replace('.', '')
        return eval(numero_str)


    def procces_gpd(self, texto: str):
        result = re.search(r'\$([\d,.]+)(?: billion)?', str(texto))# million, billion

        if result:
            numero_str = result.group(1)
            numero_convertido = self.convertir_a_miles_millones(numero_str)
            return numero_convertido

        return None


    def get_decimal(self, texto: str):
        result = re.search(r'([\d.]+)', str(texto))

        if result:
            numero = result.group(1)
            return numero

        return None

    def get_population(self, text: str) -> str:
        if re.match(r'\d+,\d+,\d+', text): 
            resultado = re.search(r'^(.*?)(?=\()', str(text))
            if resultado:
                texto_cortado = resultado.group(1).strip().split(",")
                return "".join(texto_cortado)
        else:
            # Dividir el texto en oraciones
            oraciones = re.split(r'[.!?]', text)
            # Expresión regular para buscar números sin paréntesis y sin comas
            patron_numeros = r'(?<!\()\b\d{1,3}(?:,\d{3})*\b(?!\))'
            numeros = []
            for oracion in oraciones:
                numeros.extend(re.findall(patron_numeros, oracion))
            numeros_sin_comas = [numero.replace(',', '') for numero in numeros]
            suma_total = sum(int(numero) for numero in numeros_sin_comas)
            return str(suma_total)

        return text
 