import discord
from discord.ext import commands, tasks
import youtube_dl
import os


#keyInfo = open("/Users/anthony/PycharmProjects/CSE442/keys", "r")
my_secret = "ODg3Nzc5MTk4OTM5MzEyMTI4.YUJGzw.r0IgYyX4cTXC-gugnVuautrtKj4"

client = commands.Bot(command_prefix='/')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(pass_context=True)
async def hello(cxt):
    await cxt.send("Hello World!")


@client.command(pass_context=True)
async def TheWeekend(cxt):
    return

@client.command(pass_context=True)
async def ping(cxt):
    await cxt.send("Pong!")
    print("hey")


client.run(my_secret)
