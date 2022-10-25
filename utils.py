import subprocess
from urllib import response
import requests

def abrirChrome(url: str = 'https://www.google.com/'):
    subprocess.Popen(
        [
        'C:\Program Files\Google\Chrome\Application\chrome.exe',
        url
        ]
    )

def abrirVSCode(dest: str = '.'):
    subprocess.Popen(
        [
        r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe',
        '-c',
        'code',
        dest
        ]
    )

def abrirExcel(file: str = ''):
    subprocess.Popen(
        [
        r'C:\Program Files (x86)\Microsoft Office\Office16\EXCEL.EXE',
        file
        ]
    )

def abrirWord(file: str = ''):
    subprocess.Popen(
        [
        r'C:\Program Files (x86)\Microsoft Office\Office16\WINWORD.EXE',
        file
        ]
    )

def pegarPrevisao(city_name: str = None):
    params = {
        'key': open('.hgbrasil_api_key').read(),
        'fields': 'temp,city_name,description'
    }
    if city_name:
        params['city_name'] = city_name
    else:
        params['user_ip'] = 'remote'
    response = requests.get('https://api.hgbrasil.com/weather', params=params)
    return response.json()['results']

def pegarCotação():
    response = requests.get('https://economia.awesomeapi.com.br/json/USD-BRL/1')
    return response.json()[0]['bid']

def pesquisaNoGoogle(search : str = ''):
    if search.strip() != '':
        params = {
            'key': open('.google_api_key').read(),
            'query': search,
            'limit': 1
        }
        response = requests.get('https://kgsearch.googleapis.com/v1/entities:search', params=params)
        return response.json()

if __name__ == '__main__':
    # abrirChrome('https://www.google.com/search?q=Teste aqui')
    # abrirVSCode(r"C:\Users\johan.kneubuhler\Desktop")
    # abrirExcel(r'C:\Users\johan.kneubuhler\Downloads\frutas.csv')
    # abrirWord(r'C:\Users\johan.kneubuhler\Downloads\teste.docx')

    # pegarPrevisao('Jaraguá do Sul,SC')
    # pegarPrevisao('Massaranduba,SC')
    # print(pegarPrevisao('Schroeder,SC'))
    # print(pegarCotação())
    print(pesquisaNoGoogle('teste'))