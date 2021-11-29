import os
from bot import Bot
import fileinput

port = '8080'
"""
if os.environ.get('PORT') != None:
    port = os.environ.get('PORT')
textToSearch = 'DYNAMICPORT'
fileToSearch = "bot/application.yml"
tempFile = open( fileToSearch, 'r+' )

for line in fileinput.input(fileToSearch):
    if line.__contains__(textToSearch):
        tempFile.write( line.replace( textToSearch, port ) )
tempFile.close()
"""
bot = Bot(prefix='/', lavalinkpass="password", lavalinkport=int(port))

my_secret = os.environ.get('TOKEN')

bot.connect(my_secret)
