import os
from bot import Bot
import fileinput

ON_HEROKU = os.environ.get('ON_HEROKU')
port = '8080'
if ON_HEROKU:
    port = os.environ.get('PORT')
    textToSearch = 'DYNAMICPORT'
    fileToSearch  = "bot/application.yml"
    tempFile = open( fileToSearch, 'r+' )

    for line in fileinput.input(fileToSearch):
        tempFile.write( line.replace( textToSearch, port ) )
    tempFile.close()

bot = Bot(prefix='$', lavalinkpass="password", lavalinkport=int(port))

my_secret = os.environ.get('TOKEN')

bot.connect(my_secret)
