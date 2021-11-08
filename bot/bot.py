from discord.ext import commands
import os
from threading import Thread
import time
from music import Music
import discord
from ytapi import *
from artist_info import *

commandsList = ["hello: I wont leave you hanging", 
                "ping: pOnG", 
                "helpme: I assume you've already figured this out",
                "play (Song Title): I can play a song for you as long as you are in a voice chat!",
                "topsongs (Artist Name): I'll show you the top ten songs of whatever artist you choose",
                "url (Song Title): I can grab a youtube url of whatever song you like!",
                "topalbums (Artist Name): I can list an artist's top albums.",
                "relatedartists (Artist Name): I can show you a bunch of artists similar to the one you requested!",
                "getGenre (Artist Name): I can display some information about what genres this artists fits into!",
                "artistPic (Artist Name): I can show you a picture of the artist you request.", 
				"pause: Pauses the song. Do /play to unpause!",
				"clear: Clears the queue",
				"skip: Skips the song",
                "disconnect: Later!"]

#This class is used to get the body started along with lavalink, the music playing application we use.
class Bot:
	def __init__(self, **kwargs):
		self.intents = discord.Intents.default()
		self.intents.members = True
		if "prefix" not in kwargs:
			raise "You must provide a prefix"
		else:
			self.bot = commands.Bot(command_prefix = kwargs["prefix"], intents = self.intents)
			self.bot.lavalinkpass = kwargs["lavalinkpass"]
			self.bot.lavalinkport = kwargs["lavalinkport"]

	def connect(self, token):
		def lavarun():
			os.system("java -jar Lavalink.jar")
		
		print("Starting processes!")
		time.sleep(5)
		print("Running Lavalink.")
		Thread(target = lavarun).start()
		time.sleep(30) # yep i intentionally used a blocking module
		# lavalink takes a while to boot up
		# so this is to make sure its ready when bot gets ready
		self.bot.add_cog(init(self.bot))
		print("-------------------------------\nRunning Bot!")
		self.bot.run(token)

#This is the main body of the bot itself. The music player functionality is within a different file.
class init(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print("The bot is ready!")
		self.bot.add_cog(Music(self.bot))

	# Bot Command: /helpme
	# Purpose: Displays a message containing all available bot commands a discord server member may utilize.
	@commands.command(pass_context=True)
	async def helpme(self, ctx):
		currentCommands = "Hi I'm Discify, your all-purpose Discord Music Bot! \n Here's what I can do if you type /(command): \n"
		for i in commandsList:
			currentCommands += i + "\n"
		await ctx.send(currentCommands)


	# Bot Command: /topsongs
	# Purpose: The Spoitfy API call made by Billy returns back the artistDict and the bot prints out "top songs".
	@commands.command(pass_context=True)
	async def topsongs(self, ctx, *namelst):
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
	@commands.command(pass_context=True)
	async def url(self, ctx, *querylst):
		# Get user query
		query = " ".join(querylst)

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
	@commands.command(pass_context=True)
	async def topalbums(self, ctx, *querylist):
		# Get user query
		query = " ".join(querylist)

		# Get artist's top albums from Spotify API
		data = getTopAlbums(query)

		# Create string the bot will print
		spoken_str = 'Top Albums from ' + query + ':\n'
		for i in data:
			spoken_str += '• ' + i['name'] + '\n'
		spoken_str += '\n'

		# Bot prints the string
		await ctx.send(spoken_str)


	# Bot Command: /relatedartists
	# Purpose: Returns related artists to a user entered artist.
	@commands.command(pass_context=True)
	async def relatedartists(self, ctx, *querylist):
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


	# Bot Command: /artistPic
	# Purpose: Returns artist pic of a user entered artist.
	@commands.command(pass_context=True)
	async def artistPic(self, ctx, *querylist):
		query = " ".join(querylist)
		data = getArtistImage(query)
		bottext = 'This is ' + query + ':\n'
		await ctx.send(bottext)
		await ctx.send(data)


	# Bot Command: /getGenre
	# Purpose: Returns genre of a user entered artist.
	@commands.command(pass_context=True)
	async def getGenre(self, ctx, *querylist):
		query = " ".join(querylist)
		data = getArtistGenre(query)
		bottext = 'Here is the genre information I could find from Spotify on ' + query + '! \n ' \
																						'If you want to dive into ' \
																						'genres, checkout this cool ' \
																						'site https://everynoise.com/ \n'
		for v in data:
			bottext += '-' + v + '\n'
		await ctx.send(bottext)


	@commands.command(pass_context=True)
	async def hello(self, ctx):
		await ctx.send("Hello World!")


	@commands.command(pass_context=True)
	async def ping(self, cxt):
		await cxt.send("Pong!")