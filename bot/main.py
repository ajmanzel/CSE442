import os
import discord
from discord.ext import commands, tasks
from discord.player import FFmpegAudio
import music
from artist_info import getTop10Songs, getTopAlbums
from ytapi import get_youtube_data

# from KEYS.disctoken import *    # Download the discKEYS file and put it in the ./CSE442/discord directory. Personal testing

my_secret = os.environ.get('TOKEN')
# my_secret = TOKEN   # Comment this out before pushing please

client = commands.Bot(command_prefix='/')

intents = discord.Intents.all()
cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup(client)

commandsList = ["hello: I wont leave you hanging", "ping: pOnG", 
                "helpme: I assume you've already figured this out",
                "topsongs (Artist Name): I'll show you the top ten songs of whatever artist you choose",
                "url (Song Title): I can grab a youtube url of whatever song you like!",
                "play (Song Title): I can play a song for you as long as you are in a voice chat!"
                "albums (Artist Name): I can list an artist top albums.", 
                "goodbye: Later!"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(pass_context=True)
async def hello(ctx):
    await ctx.send("Hello World!")


@client.command(pass_context=True)
async def helpme(ctx):
    currentCommands = "Hi I'm Discify, your all-purpose Discord Music Bot! \n Here's what I can do if you type /(command): \n"
    for i in commandsList:
        currentCommands += i + "\n"
    await ctx.send(currentCommands)


# This is how the bot calls topsongs. The API call made by Billy returns back the artistDict and the bot prints out "top songs"
@client.command(pass_context=True)
async def topsongs(ctx, *namelst):
    name = " ".join(namelst)
    artistDict = getTop10Songs(name)
    topsongsList = artistDict["top songs"]
    spokenStr = "Here are " + name + "'s top songs:\n"
    for i in topsongsList:
        if i == topsongsList[len(topsongsList) - 1]:
            spokenStr += i
        else:
            spokenStr += i + ",\n"
    await ctx.send(spokenStr)


# Currently the issue this faces is within the API call itself. The name given to the bot can get confused and the API
# returned may be a different artist that was close enough to the spelling. We gottta make sure to fix this.


# This is how the bot calls play. The API call made in ytapi.py returns the youtube_dict and the bot prints out the YouTube URL.
@client.command(pass_context=True)
async def url(ctx, *querylst):
    query = " ".join(querylst)
    data = get_youtube_data(query)
    youtube_url = data['video_url']
    youtube_url = data['video_url']
    title = data['title']
    artist = data['artist']
    spoken_str = 'YouTube URL: ' + youtube_url + '\n"' + title + '" by ' + artist
    await ctx.send(spoken_str)


@client.command(pass_context=True)
async def albums(ctx, *querylist):
    query = " ".join(querylist)
    data = getTopAlbums(query)
    spoken_str = "N/A"
    await ctx.send(spoken_str)


@client.command(pass_context=True)
async def ping(cxt):
    await cxt.send("Pong!")


client.run(my_secret)
