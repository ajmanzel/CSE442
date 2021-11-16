import os
from bot import Bot

ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    port = int(os.environ.get('PORT', 17995))
else:
    port = 8080

bot = Bot(prefix='/', lavalinkpass="password", lavalinkport=port)

my_secret = os.environ.get('TOKEN')
bot.connect(my_secret)
