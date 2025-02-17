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
        
    def limpiar_campos(self, text: str) -> float:
        result = re.search(r'([\d,.]+)(?:\s*(?:%|sq km|years))?', str(text))

        if result:
            extracted_number = result.group(1)

            if '(' in text and ')' in text:
                return 0

            if ',' in extracted_number:
                number = extracted_number.replace(',', '')
                return float(number)
            else:
                return float(extracted_number)

        return 0

    def limpiar(self, text: str) -> float:
        result = re.search(r'(-?[\d,]+)\s*m?', text)

        if result:
            extracted_number = result.group(1)
            if ',' in extracted_number:
                number = extracted_number.replace(',', '')
                return float(number) if number != '' else 0
            else:
                return float(result.group(1))

        return 0


    def limpiar_porcentaje(self, text: str) -> float:
        result = re.search(r'([\d.]+)%', str(text))

        if result:
            extracted_number = result.group(1)
            return float(extracted_number)

        return 0


    def procces_gpd(self, text: str) -> float:
        if 'million' in text:
            result = re.search(r'\$([\d,.]+)(?: million)?', str(text))# million
            if result:
                numero_str = result.group(1)
                #numero_convertido = convertir_a_miles_millones(numero_str)
                return float(numero_str) * 1.0e6
            return 0
        elif 'billion' in text:
            result = re.search(r'\$([\d,.]+)(?: billion)?', str(text))# billion
            if result:
                numero_str = result.group(1)
                #numero_convertido = convertir_a_miles_millones(numero_str)
                return float(numero_str) * 1.0e9
            return 0
        return 0


    def get_decimal(self, texto: str):
        result = re.search(r'([\d.]+)', str(texto))

        if result:
            numero = result.group(1)
            return numero

        return 0

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

        return 0
 