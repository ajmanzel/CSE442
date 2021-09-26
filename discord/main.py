import discord
from discord.ext import commands, tasks
import youtube_dl
import os
import spotify.artist_info #I was required to turn spotify into a package with the use of the init
#                           file. Do not remove __init__.py from spotify or else this will no longer work.
#from discKEYS.disctoken import *
# Download the discKEYS file and put it in the ./CSE442/discord directory. Personal testing


my_secret = os.environ.get('TOKEN')
#my_secret = TOKEN
#

client = commands.Bot(command_prefix='/')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(pass_context=True)
async def hello(cxt):
    await cxt.send("Hello World!")

# This is how the bot calls topsongs. The API call made by Billy returns back the artistDict and the bot prints out "top songs"
@client.command(pass_context=True)
async def topsongs(cxt, name: str):
    artistDict = spotify.artist_info.getAll(name)
    topsongsList = artistDict["top songs"]
    spokenStr = "Here are " + name + "'s top songs:\n"
    for i in topsongsList:
        if i == topsongsList[len(topsongsList)-1]:
            spokenStr += i
        else:
            spokenStr += i + ",\n"
    await cxt.send(spokenStr)
# Currently the issue this faces is within the API call itself. The name given to the bot can get confused and the API
# returned may be a different artist that was close enough to the spelling. We gottta make sure to fix this.


@client.command(pass_context=True)
async def ping(cxt):
    await cxt.send("Pong!")
    print("hey")


client.run(my_secret)
