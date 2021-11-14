from discord.ext import commands
import os
from threading import Thread
import time
from music import Music
import discord
from ytapi import *
from artist_info import *

# Global list containing all availble bot commands
commandsList = ["hello: I wont leave you hanging", 
                "ping: pOnG", 
                "helpme: I assume you've already figured this out",
				"play (Song Title): I can play a song for you as long as you are in a voice chat!", 
				"pause: Pauses the song. Do /play to unpause!",
				"clear: Clears the queue",
				"skip: Skips the song",
                "disconnect: Later!",
                "topsongs (Artist Name): I'll show you the top ten songs of whatever artist you choose",
                "url (Song Title): I can grab a youtube url of whatever song you like!",
                "topalbums (Artist Name): I can list an artist's top albums.",
                "relatedartists (Artist Name): I can show you a bunch of artists similar to the one you requested!",
                "getGenre (Artist Name): I can display some information about what genres this artists fits into!",
                "artistPic (Artist Name): I can show you a picture of the artist you request."]


# Helper function to create embedded message
def created_embedded_msg(title, description, color, name, value, inline):
	# Create embedded message
	embedded_msg = discord.Embed(
				title = title,
				description = description,
				color = color
			)
	embedded_msg.add_field(name=name, value=value, inline=inline)

	# Return embedded message
	return embedded_msg


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
		# Initialize variables
		title = "Help"
		description = "Hi I'm Discify, your all-purpose Discord Music Bot!\nHere's what I can do if you type /(command):\n"
		color = 0x1DB954
		commands = ""

		# Format commandsList into string
		for command in commandsList:
			commands += "• " + command + "\n"

		# Create embedded message
		spoken_str = created_embedded_msg(title, description, color, "", commands, True)
		
		# Send embedded message
		await ctx.send(embed = spoken_str)


	# Bot Command: /topsongs
	# Purpose: Displays a message containing a user entered artist's top 10 songs.
	@commands.command(pass_context=True)
	async def topsongs(self, ctx, *querylist):
		# Initialize variables
		artist = " ".join(querylist)
		title = "Top 10 Songs"
		description = "Here are " + artist + "'s top 10 songs:\n"
		color = 0x1DB954
		songs = ""

		# Get artist's top 10 songs from Spotify API
		top10_list = getTop10Songs(artist)
		
		# Format top10_list into string
		for song in top10_list:
			songs += "• " + song + "\n"

		# Create embedded message
		spoken_str = created_embedded_msg(title, description, color, "", songs, True)

		# Send embedded message
		await ctx.send(embed = spoken_str)


	# Bot Command: /url
	# Purpose: Returns the song title, channel name, and YouTube url from a user entered song.
	@commands.command(pass_context=True)
	async def url(self, ctx, *querylist):
		# Get user query
		query = " ".join(querylist)

		# Get song data from YouTube API
		data = get_youtube_data(query)

		# Create string the bot will print
		youtube_url = data['video_url']
		title = data['title']
		artist = data['artist']
		spoken_str = '"' + title + '" by ' + artist + '\nYouTube URL: ' + youtube_url

		# Send message string
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
		title = "Related Artists"
		description = "Related Artists to " + query + ":\n"
		color = 0x1DB954
		artists = ""

		# Get artist's related artists from Spotify API
		data = getRelatedArtists(query)

		# Create string the bot will print
		for i in data:
			artists += '• ' + i + '\n'

		spoken_str = created_embedded_msg(title, description, color, "", artists, True)

		# Bot prints the string
		await ctx.send(embed=spoken_str)


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