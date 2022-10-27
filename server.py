import logging
from tkinter import Button, Label, Tk

import speech_recognition as sr

import acao
import saudacao
import utils

# initialize the recognizer
r = sr.Recognizer()


def start_recording():
    logging.info('botão clicado')
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
            # elif response['app'] == 'pesquisarGoogle':

            # elif response['app'] == 'previsao':
            elif response['app'] == 'cotação':
                response = utils.pegarCotação()
                utils.speak(
                    'A cotação do dolar hoje é de aproximadamente {} reais'.format(
                        response
                    )
                )

        # if 'previsão' in input:
        #     output = utils.pegarPrevisao(input)
        #     print(output)
        #     tts = gTTS(output['description'], lang='pt-br')
        #     tts.save("output.mp3")
        #     playsound("output.mp3")
        # elif 'chrome' in input:
        #     utils.abrirChrome()
        # elif 'visual studio code' in input:
        #     utils.abrirVSCode()
        # elif 'excel' in input:
        #     utils.abrirExcel()
        # elif 'word' in input:
        #     utils.abrirWord()
        # elif 'cotação' in input:
        #     utils.pegarCotação()
        # elif 'google' in input:
        #     utils.pesquisaNoGoogle(input)
    """ print('botão clicado')
    with sr.Microphone() as source:
    # listen for the data (load audio to memory)
        audio_data = r.listen(source)
    # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language='pt-BR')
        myobj = {'input': text}
        print(type(text).__name__)
        if 'previsão' in text:
            x = requests.post(url_previsao, myobj)
            print(x) """


janela = Tk()

texto = Label(text='Live de Python')
texto.pack()

botao = Button(text='clique aqui', command=start_recording)
botao.pack()

janela.mainloop()
