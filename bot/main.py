import os
from bot import Bot
from Naked.toolshed.shell import execute_js

ON_HEROKU = os.environ.get('ON_HEROKU')
port = 8080
if ON_HEROKU:
    success = execute_js('bootstrap.js')
    port = int(os.environ.get('PORT'))

bot = Bot(prefix='$', lavalinkpass="password", lavalinkport=port)

my_secret = os.environ.get('TOKEN')

bot.connect(my_secret)
