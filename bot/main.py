import discord
from discord.ext import commands, tasks
from discord.player import FFmpegAudio
import youtube_dl
import os
import artist_info
from ytapi import get_youtube_data
#from KEYS.disctoken import *    # Download the discKEYS file and put it in the ./CSE442/discord directory. Personal testing

my_secret = os.environ.get('TOKEN')
#my_secret = TOKEN   # Comment this out before pushing please

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


# This is how the bot calls play. The API call made in ytapi.py returns the youtube_dict and the bot prints out the YouTube URL.
@client.command(pass_context=True)
async def play(cxt, query: str):
    youtube_dict = get_youtube_data(query)
    youtube_url = youtube_dict['video_url']
    spoken_str = "YouTube URL: " + youtube_url
    await cxt.send(spoken_str)


@client.command(pass_context=True)
async def ping(cxt):
    await cxt.send("Pong!")

@client.command(pass_context=True)
async def playsong(cxt, url: str):
    #cxt.voice_client.stop()
    if cxt.author.voice is None:
        await cxt.send("You're not in a voice channel!")
    voice_channel = cxt.author.voice.channel
    if cxt.voice_client is None:
        await voice_channel.connect()
    else:
        await cxt.voice_channel.move_to(voice_channel)


    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }
    YDL_OPTIONS = {
        'format': 'bestaudio'
    }
    vc = cxt.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)

@client.command(pass_context=True)
async def goodbye(cxt):
    await client.voice_client.disconnect()
    await cxt.send("Goodbye!")


client.run(my_secret)
