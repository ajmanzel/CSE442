import os
from bot import Bot

ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    port = int(os.environ.get('PORT', 17995))
    heroku = "bot/applicationOpp.yml"
    tmp_file_name = "/switching.yml"
    local = "bot/application.yml"
    os.rename(local, tmp_file_name)
    os.rename(heroku, local)
    os.rename(local, heroku)
else:
    port = 8080

bot = Bot(prefix='/', lavalinkpass="password", lavalinkport=port)

my_secret = os.environ.get('TOKEN')
bot.connect(my_secret)
