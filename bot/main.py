import discord
from discord.ext import commands, tasks
import youtube_dl
import os
import artist_info

#from KEYS.disctoken import *    # Download the discKEYS file and put it in the ./CSE442/discord directory. Personal testing

my_secret = os.environ.get('TOKEN')
# my_secret = token  # Comment this out before pushing please

client = commands.Bot(command_prefix='/')
commandsList = ["hello: I wont leave you hanging", "ping: pOnG", "helpme: I assume you've already figured this out", "topsongs (Artist Name): I'll show you the top ten songs of whatever artist you choose"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(pass_context=True)
async def hello(cxt):
    await cxt.send("Hello World!")


@client.command(pass_context=True)
async def helpme(cxt):
    currentCommands = "Hi I'm Discify, your all-purpose Discord Music Bot! \n Here's what I can do if you type /(command): \n"
    for i in commandsList:
        currentCommands += i + "\n"
    await cxt.send(currentCommands)


# This is how the bot calls topsongs. The API call made by Billy returns back the artistDict and the bot prints out "top songs"
@client.command(pass_context=True)
async def topsongs(cxt, name: str):
    artistDict = artist_info.getAll(name)
    topsongsList = artistDict["top songs"]
    spokenStr = "Here are " + name + "'s top songs:\n"
    for i in topsongsList:
        if i == topsongsList[len(topsongsList) - 1]:
            spokenStr += i
        else:
            spokenStr += i + ",\n"
    await cxt.send(spokenStr)


# Currently the issue this faces is within the API call itself. The name given to the bot can get confused and the API
# returned may be a different artist that was close enough to the spelling. We gottta make sure to fix this.


@client.command(pass_context=True)
async def ping(cxt):
    await cxt.send("Pong!")



client.run(my_secret)
