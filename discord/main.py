import discord
from discord.ext import commands, tasks
import youtube_dl
import os

# from discKEYS.disctoken import *

my_secret = os.environ.get('TOKEN')

client = commands.Bot(command_prefix='/')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(pass_context=True)
async def hello(cxt):
    await cxt.send("Hello World!")


@client.command(pass_context=True)
async def topsongs(cxt, name: str):
    return


@client.command(pass_context=True)
async def ping(cxt):
    await cxt.send("Pong!")
    print("hey")


client.run(my_secret)
