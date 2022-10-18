from tkinter import Tk, Label, Button
import speech_recognition as sr
import requests

#filename = "WhatsApp-Ptt-2022-10-11-at-20.36.13.wav"

url_previsao = 'https://localhost:3000/test'

# initialize the recognizer
r = sr.Recognizer()

# open the file
def fui_clicado():
    print('botão clicado')
    with sr.Microphone() as source:
    # listen for the data (load audio to memory)
        audio_data = r.listen(source)
    # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language='pt-BR')
        myobj = {'input': text}
        print(type(text).__name__)
        if 'previsão' in text:
            x = requests.post(url_previsao, myobj)
            print(x)
janela = Tk()

texto = Label(text='Live de Python')
texto.pack()

botao = Button(text='clique aqui', command=fui_clicado)
botao.pack()

janela.mainloop()