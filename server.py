import logging
from tkinter import END, Button, Entry, Label, Tk, Frame, BOTTOM

import speech_recognition as sr

import acao
import saudacao
import utils

logging.basicConfig(level='INFO')

# initialize the recognizer
r = sr.Recognizer()


def start_recording():
    with sr.Microphone() as source:
        audio_data = r.listen(source)
        input = r.recognize_google(audio_data, language='pt-BR')
        input = input.lower()
        logging.info(input)
        response = saudacao.identificar(input)
        if response['success']:
            input = response['input']
            logging.info(input)
            response = acao.identificar(input)
            logging.info(response)
            if response['app'] == 'vscode':
                utils.abrirVSCode()
                utils.speak('Visual Studio Code aberto')
            elif response['app'] == 'word':
                success = utils.abrirWord()
                if success:
                    utils.speak('Microsoft Office Word aberto')
                else:
                    utils.speak(
                        'Ocorreu algum problema ao abrir Microsoft Office Word'
                    )
            elif response['app'] == 'excel':
                success = utils.abrirExcel()
                if success:
                    utils.speak('Microsoft Office Excel aberto')
                else:
                    utils.speak(
                        'Ocorreu algum problema ao abrir Microsoft Office Excel'
                    )
            elif response['app'] == 'chrome':
                url = 'https://www.google.com/'
                if 'url' in response['variables'].keys():
                    url = response['variables']['url']
                success = utils.abrirChrome(url=url)
                if success:
                    utils.speak('Google Chrome aberto no site {}'.format(url))
                else:
                    utils.speak(
                        'Ocorreu algum problema ao abrir Google Chrome'
                    )
            elif response['app'] == 'pesquisarGoogle':
                search = ''
                if 'search' in response['variables'].keys():
                    search = response['variables']['search']
                response = utils.pesquisaNoGoogle(search=search)
                if response:
                    logging.info(response)
                    responseText = None
                    if 'itemListElement' in response.keys():
                        if len(response['itemListElement']) > 0:
                            responseText = response['itemListElement'][0][
                                'result'
                            ]['detailedDescription']['articleBody']
                    if responseText:
                        utils.speak(responseText)
                    else:
                        utils.speak(
                            'Ocorreu algum problema na pesquisa por {}'.format(
                                search
                            )
                        )
                else:
                    utils.speak(
                        'Ocorreu algum problema na pesquisa por {}'.format(
                            search
                        )
                    )
            elif response['app'] == 'previsao':
                city = None
                if 'city' in response['variables'].keys():
                    city = response['variables']['city']
                response = utils.pegarPrevisao(city_name=city)
                logging.info(response)
                if response:
                    utils.speak(
                        'Previsão do tempo para {} é de {} com aproximadamente {} graus'.format(
                            response['city_name'],
                            response['description'],
                            response['temp'],
                        )
                    )
                else:
                    utils.speak(
                        'Ocorreu algum problema na procura por previsão do tempo da cidade {}'.format(
                            city
                        )
                    )
            elif response['app'] == 'cotação':
                response = utils.pegarCotação()
                utils.speak(
                    'A cotação do dolar hoje é de aproximadamente {} reais'.format(
                        response
                    )
                )
            elif response['app'] == 'tradutor':
                text = None
                if 'text' in response['variables'].keys():
                    text = response['variables']['text']
                if text:
                    response = utils.translate(text=text)
                    utils.speak(response, lang='en')
                else:
                    utils.speak(
                        'Ocorreu algum problema na hora de identificar o texto a traduzir de {}'.format(
                            text
                        )
                    )
            elif response['app'] == 'lembrete':
                text = None
                if 'text' in response['variables'].keys():
                    text = response['variables']['text']
                if text:
                    global lembretes_quantity
                    lembretes_quantity += 1
                    entry = Entry(frame)
                    entry.grid(row=lembretes_quantity, column=1)
                    entry.insert(END, '{} - {}'.format(lembretes_quantity - 1, text))
                    utils.speak(
                        'Adicionado lembrete {}'.format(
                            text
                        )
                    )
                else:
                    utils.speak(
                        'Ocorreu algum problema na hora de adicionar o lembrete {}'.format(
                            text
                        )
                    )


janela = Tk()

texto = Label(text='Clique no botão a baixo e fale com o Ronaldo')
texto.pack()

botao = Button(text='Iniciar gravação!', command=start_recording)
botao.pack()

frame = Frame(janela)
entry = Entry(frame)
entry.grid(row=1, column=1)
entry.insert(END, 'Lembretes')
frame.pack()
lembretes_quantity = 1
janela.title('Ronaldo - Assistente virtual')
janela.mainloop()
