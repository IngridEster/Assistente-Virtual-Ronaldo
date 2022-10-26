from tkinter import Tk, Label, Button
import speech_recognition as sr
import requests
import utils
from gtts import gTTS
from playsound import playsound
import os 


filename = "WhatsApp-Ptt-2022-10-25-at-20.21.46.wav"

# initialize the recognizer
r = sr.Recognizer()

# open the file
def fui_clicado():
    print('botão clicado')
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        input = r.recognize_google(audio_data, language='pt-BR')
        input = input.lower()
        print(input)
        if 'previsão' in input:
            output = utils.pegarPrevisao(input)
            print(output)
            tts = gTTS(output['description'], lang='pt-br')
            tts.save("output.mp3")
            playsound("output.mp3")
        elif 'chrome' in input:
            utils.abrirChrome()
        elif 'visual studio code' in input:
            utils.abrirVSCode()
        elif 'excel' in input:
            utils.abrirExcel()
        elif 'word' in input:
            utils.abrirWord()
        elif 'cotação' in input:
            utils.pegarCotação()
        elif 'google' in input:
            utils.pesquisaNoGoogle(input)
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

botao = Button(text='clique aqui', command=fui_clicado)
botao.pack()

janela.mainloop()