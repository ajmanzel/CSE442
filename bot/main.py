import os
import discord
from discord.ext import commands, tasks
from botqueue import botQueue
from discord.player import FFmpegAudio
import music
from artist_info import getTop10Songs, getTopAlbums, getArtistImage, getArtistGenre
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
                "play (Song Title): I can play a song for you as long as you are in a voice chat!",
                "topsongs (Artist Name): I'll show you the top ten songs of whatever artist you choose",
                "url (Song Title): I can grab a youtube url of whatever song you like!",
                "topalbums (Artist Name): I can list an artist's top albums.",
                "relatedartists (Artist Name): I can show you a bunch of artists similar to the one you requested!",
                "getGenre (Artist Name): I can display some information about what genres this artists fits into!",
                "artistPic (Artist Name): I can show you a picture of the artist you request.", "goodbye: Later!"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    client.queue = botQueue
    client.queue.__init__(client.queue, client)


@client.command(pass_context=True)
async def hello(ctx):
    await ctx.send("Hello World!")


# Bot Command: /helpme
# Purpose: Displays a message containing all available bot commands a discord server member may utilize.
@client.command(pass_context=True)
async def helpme(ctx):
    currentCommands = "Hi I'm Discify, your all-purpose Discord Music Bot! \n Here's what I can do if you type /(command): \n"
    for i in commandsList:
        currentCommands += i + "\n"
    await ctx.send(currentCommands)


# Bot Command: /topsongs
# Purpose: The Spoitfy API call made by Billy returns back the artistDict and the bot prints out "top songs".
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


# Bot Command: /url
# Purpose: Returns the song title, channel name, and YouTube url from a user entered song.
@client.command(pass_context=True)
async def url(ctx, *querylist):
    # Get user query
    query = " ".join(querylist)

    # Get song data from YouTube API
    data = get_youtube_data(query)

    # Create string the bot will print
    youtube_url = data['video_url']
    title = data['title']
    artist = data['artist']
    spoken_str = '"' + title + '" by ' + artist + '\nYouTube URL: ' + youtube_url

    # Bot prints the string
    await ctx.send(spoken_str)


# Bot Command: /topalbums
# Purpose: Returns top albums from a user entered artist.
@client.command(pass_context=True)
async def topalbums(ctx, *querylist):
    # Get user query
    query = " ".join(querylist)

    # Get artist's top albums from Spotify API
    data = getTopAlbums(query)

    # Create string the bot will print
    spoken_str = 'Top Albums from ' + query + ':\n'
    data = getTopAlbums(query)
    for i in data:
        spoken_str += '• ' + i['name'] + '\n'
    spoken_str += '\n'

    # Bot prints the string
    await ctx.send(spoken_str)


# Bot Command: /relatedartists
# Purpose: Returns related artists to a user entered artist.
@client.command(pass_context=True)
async def relatedartists(ctx, *querylist):
    # Get user query
    query = " ".join(querylist)

    # Get artist's related artists from Spotify API
    data = getRelatedArtists(query)

    # Create string the bot will print
    spoken_str = 'Related Artists to ' + query + ':\n'
    for i in data:
        spoken_str += '• ' + i + '\n'
    spoken_str += '\n'

    # Bot prints the string
    await ctx.send(spoken_str)


@client.command(pass_context=True)
async def artistPic(ctx, *querylist):
    query = " ".join(querylist)
    data = getArtistImage(query)
    bottext = 'This is ' + query + ':\n'
    await ctx.send(bottext)
    await ctx.send(data)


@client.command(pass_context=True)
async def getGenre(ctx, *querylist):
    query = " ".join(querylist)
    data = getArtistGenre(query)
    bottext = 'Here is the genre information I could find from Spotify on ' + query + '! \n ' \
                                                                                      'If you want to dive into ' \
                                                                                      'genres, checkout this cool ' \
                                                                                      'site https://everynoise.com/ \n'
    await ctx.send(bottext)
    await ctx.send(data)


@client.command(pass_context=True)
async def ping(cxt):
    await cxt.send("Pong!")


client.run(my_secret)
