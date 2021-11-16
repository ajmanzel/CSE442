import os
from bot import Bot

ON_HEROKU = os.environ.get('HEROKU_ON')

if HEROKU_ON:
    port = int(os.environ.get('PORT'))
else:
    port = 8080

bot = Bot(prefix='/', lavalinkpass="password", lavalinkport=port)

my_secret = os.environ.get('TOKEN')
bot.connect(my_secret)
