from chatterbot.chatterbot import ChatBot
from pep8 import readlines
from chatterbot.trainers import ListTrainer  # method to train the chatbot

bot = ChatBot('Test')  # create the chatbot

conv = open('chat.txt', 'r').readlines()

while True:
    bot.set_trainer(ListTrainer)  # set the trainers
    bot.train(conv)  # train the bot
    request = input('You: ')
    response = bot.get_response(request)
    print('Bot: ', response)
    
