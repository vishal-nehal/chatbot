# pip install chatterbot
# pip install chatterbot_corpus
# pip install pyttsx3
#pip install pypiwin32 , error ko remove krne ke liye
# pyttsx3 library audio functons of use krne k liye krtey hai
#pip install SpeechRecognition
#user input dega through speak
#pip install pyaudio
# microphone ke through input dene ke liye like earphone ke through bolne pe

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
from chatterbot.trainers import ChatterBotCorpusTrainer


bot = ChatBot("Bot")
convo = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot , i am created by Vishal',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in lucknow',
    'In which language you talk?',
    ' I mostly talk in english'
]
trainer = ListTrainer(bot)
trainer.train(convo)
# answer = bot.get_response("How are you doing these days ")
# print(answer)

# print("Talk to Bot")
# while True:
#     query = input()
#     if query =='exit':
#         break
#     answer = bot.get_response(query)
#     print("Bot Replying ......",answer)

# trainer = ChatterBotCorpusTrainer(bot)
#
# trainer.train(
#     "chatterbot.corpus.english"
# )

main = Tk()
main.geometry("500x650")
main.title("My chatterBot")
img = PhotoImage(file ="telegra_Image.png")
photoL = Label(main , image = img)
photoL.pack(pady = 5)


engine = pp.init()
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voices', voices[0].id)
#voices[0]  means female voice

def speak(word):
    engine.say(word)
    engine.runAndWait()

# create takeQuery function : it takes audio as a input from user and convert it to string
# def takeQuery():
#     sr = s.Recognizer()
#     sr.pause_threshold = 1
#     print("your bot is try to speak ")
#     with s.Microphone() as m:
#         try:
#             audio = sr.listen(m)
#             query = sr.recognize_google(audio,language='eng-in')
#             print(query)
#             textF.delete(0,END)
#             textF.insert(0,query)
#             ask_from_bot()
#         except Exception as e:
#             print(e)
#             print("Not recognize")




def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END , "You : "+query)
    msgs.insert(END , "Bot : "+str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)
# msgs.yview(END) scroll bar automatically down hota jayega apne ko messages dekhne ke liye hath se niche nhi krni pdegi


frame = Frame(main)
sc = Scrollbar(frame)

msgs = Listbox(frame, width = 80 ,height = 20 ,yscrollcommand =sc.set);
#yscrollcommand =sc.set scroll bar ko active krne ke liye kiya gya h

sc.pack(side = RIGHT , fill = Y)
msgs.pack(side = LEFT ,fill = BOTH ,pady = 10)
frame.pack()
# Making text field
textF = Entry(main, font = ("verdana",20))
textF.pack(fill = X,pady = 10)
btn = Button(main , text = "Ask from Bot", font = ("verdana",10),command = ask_from_bot)
btn.pack()

#creating a function for automatic enter ask from bot buttom

def enter_function(event):
    btn.invoke()

# going to bind main window with enter key

main.bind('<Return>',enter_function)


#ek repeat Listen function define karenge jo bar bar query ko lega  jb tk GUI ko cut na kr de

# def repeatL():
#     while True:
#         takeQuery()
#
# t = threading.Thread(target=repeatL)
#
# t.start()

main.mainloop()
