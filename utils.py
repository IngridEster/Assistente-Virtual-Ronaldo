import datetime
import logging
import os
import subprocess

import requests
from googletrans import Translator
from gtts import gTTS
from playsound import playsound


def abrirChrome(url: str = 'https://www.google.com/'):
    pathsChrome = [
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    ]
    pathChrome = None
    for path in pathsChrome:
        if os.path.exists(path):
            pathChrome = path
            break
    if pathChrome:
        subprocess.Popen([pathChrome, url])
        return True
    else:
        return False


def abrirVSCode(dest: str = '.'):
    subprocess.Popen(
        [
            r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe',
            '-c',
            'code',
            dest,
        ]
    )


def abrirExcel(file: str = ''):
    pathsExcel = [
        r'C:\Program Files (x86)\Microsoft Office\Office16\EXCEL.EXE',
        r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE',
    ]
    pathExcel = None
    for path in pathsExcel:
        if os.path.exists(path):
            pathExcel = path
            break
    if pathExcel:
        subprocess.Popen([pathExcel, file])
        return True
    else:
        return False


def abrirWord(file: str = ''):
    pathsWord = [
        r'C:\Program Files (x86)\Microsoft Office\Office16\WINWORD.EXE',
        r'C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE',
    ]
    pathWord = None
    for path in pathsWord:
        if os.path.exists(path):
            pathWord = path
            break
    if pathWord:
        subprocess.Popen([pathWord, file])
        return True
    else:
        return False


def pegarPrevisao(city_name: str = None):
    params = {
        'key': open('.hgbrasil_api_key').read(),
        'fields': 'temp,city_name,description',
    }
    if city_name:
        params['city_name'] = city_name
    else:
        params['user_ip'] = 'remote'
    response = requests.get('https://api.hgbrasil.com/weather', params=params)
    return response.json()['results']


def pegarCotação():
    response = requests.get(
        'https://economia.awesomeapi.com.br/json/USD-BRL/1'
    )
    return response.json()[0]['bid']


def pesquisaNoGoogle(search: str = ''):
    if search.strip() != '':
        params = {
            'key': open('.google_api_key').read(),
            'query': search,
            'limit': 1,
            'languages': 'pt',
        }
        response = requests.get(
            'https://kgsearch.googleapis.com/v1/entities:search', params=params
        )
        return response.json()
    else:
        return None


def translate(text: str = None):
    translator = Translator()
    return (translator.translate(text, src='pt', dest='en')).text


def speak(text: str, lang: str = 'pt'):
    date_string = datetime.datetime.now().strftime('%d%m%Y%H%M%S')
    filename = 'voice' + date_string + '.mp3'
    tts = gTTS(text, lang=lang)
    tts.save(filename)
    playsound(filename)
    os.remove(filename)


if __name__ == '__main__':
    abrirChrome('https://www.google.com/search?q=Teste aqui')
    abrirVSCode(r'C:\Users\johan.kneubuhler\Desktop')
    abrirExcel(r'C:\Users\johan.kneubuhler\Downloads\frutas.csv')
    abrirWord(r'C:\Users\johan.kneubuhler\Downloads\teste.docx')

    pegarPrevisao('Jaraguá do Sul,SC')
    pegarPrevisao('Massaranduba,SC')
    logging.debug(pegarPrevisao('Schroeder,SC'))
    logging.debug(pegarCotação())
    logging.debug(pesquisaNoGoogle('teste'))
    print(translate('teste'))
