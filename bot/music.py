from time import perf_counter
import discord
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
        split = info.split(" - ")
        artist = split[0]
        title = split[1]
        if title.__contains__("(Official"):
            title = title.split("(Official")[0]

        title = title.strip()
        artist = artist.strip()
        
        res = artist_info.botDisplay(artist_info.getAll(title, artist))
        for i in res:
            await ctx.send(i)

        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }
        YDL_OPTIONS = {
            'format': 'bestaudio'
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