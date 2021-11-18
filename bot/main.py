import os
from bot import Bot
#from Naked.toolshed.shell import execute_js

bot = Bot(prefix='$', lavalinkpass="password", lavalinkport=80)

#success = execute_js('bootstrap.js')

my_secret = os.environ.get('TOKEN')

bot.connect(my_secret)
