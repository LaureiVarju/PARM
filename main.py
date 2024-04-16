

import datetime

# Get the current date and time
current_time = datetime.datetime.now()

# Format the date and time as a string
timestamp = current_time.strftime("[%Y-%m-%d %H:%M:%S]")

# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
# Import the os module.
import os
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
# Loads the .env file that resides on the same level as the script.
load_dotenv()
# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

permissions = discord.Permissions()
permissions.update(send_messages=True, read_messages=True)
permissions_integer = permissions.value


# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.

# # intents = discord.Intents.default()
# # bot = discord.Client(intents=intents)

# intents = discord.Intents.default()
# intents.messages = True

# bot = discord.Client(intents=intents)
# # bot = discord.Client()

from discord import Intents
from discord.ext import commands

# Enable all standard intents and message content
# (prefix commands generally require message content)
intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")
	print(permissions_integer)

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	print(f"{timestamp} Received message: {message.content} in channel: {message.channel} from {message.author}")
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "hello":
		
		print("Responding to hello message")
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("hey dirtbag")

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)
