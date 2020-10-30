'''
Made by - Aditya mangal
Purpose - Python mini project
Date  - 18 october 2020
'''
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time

chatbot = ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')


print('\t\t\t A Chatot')
print('Type enrollment forms to enroll otherwise continue to talk with ChatBot')
print('You can exit by type exit\n')
while True:
    query = input(">> ")
    if 'exit' in query:
        exit()
    else:
        print(chatbot.get_response(query))
