from os import name
from time import perf_counter
from typing import Text
import discord
from discord import embeds
from discord.embeds import Embed
from discord.ext import commands
import youtube_dl
from bs4 import BeautifulSoup
import artist_info
from ytapi import get_youtube_data

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def play(self, ctx, *querylst):
        query = " ".join(querylst)
        youtube_dict = get_youtube_data(query)
        url = youtube_dict['video_url']
        titleHTML = youtube_dict['title']
        soup = BeautifulSoup(titleHTML)
        print(youtube_dict)
        if ctx.author.voice is None:
            return await ctx.send("You're not in a voice channel!")
        await ctx.send("Now playing: " + soup.text)
    
        author = ctx.author
        voice_channel = author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

        info = soup.text
        if info.__contains__('-'):
            split = info.split(" - ")
            artist = split[0]
            title = split[1]

            if title.__contains__(" ("):
                title = title.split(" (")[0]
        
            if artist.__contains__(","):
                artist = artist.split(",")[0]

            title = title.strip()
            artist = artist.strip()
        
            res = artist_info.botDisplay(artist_info.getAll(title, artist))

            info_str = title + " by " + artist

            if len(res) != 0:
                msg = discord.Embed(
                    title = info_str,
                    description = "",
                    color = 0x1DB954
                )
                msg.set_image(url=res[5])
                msg.add_field(name="Genre:", value=res[0], inline=False)
                msg.add_field(name="Top Songs:", value=res[1], inline=False)
                msg.add_field(name="Albums:", value=res[2], inline=False)
                msg.add_field(name="Similar Artists:", value=res[3], inline=False)
                msg.add_field(name="Similar Songs:", value=res[4], inline=False)

                await ctx.send(embed = msg)
            else:
                await ctx.send("No data to display.")

        else:
            await ctx.send("No data to display.")


        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }
        YDL_OPTIONS = {
            'format': '249/250/251'
        }
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command(pass_context=True)
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("Paused! ⏸")

    @commands.command(pass_context=True)
    async def resume(self, ctx):
        ctx.voice_client.resume()
        await ctx.send("Resumed! ⏯")

    @commands.command(pass_context=True)
    async def goodbye(self, ctx):
        for x in self.client.voice_clients:
            await ctx.send("Goodbye!")
            return await x.disconnect()

def setup(client):
    client.add_cog(music(client))        