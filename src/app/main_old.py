import discord
import os
import datetime


# Syntax to populate discord_token when running locally and reading from a .env file
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
# Loads the .env file that resides on the same level as the script.
load_dotenv()
# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

print(DISCORD_TOKEN)
####

# # syntax to pick up an environment variable in AWS Lambda
# DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
# WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

#lambda handler
def lambda_handler(event, context):
	print(f"event is: {event}")
	print(f"context is: {context}")
	

permissions = discord.Permissions()
permissions.update(send_messages=True, read_messages=True)
permissions_integer = permissions.value

# Discord has standardized and priviledged permissions levels, or "intents".
# Reading and writing messages in most contexts is a privileged intent that needs to be explicitly set to True in the code and enabled in the bot's permission settings in the Discord Developer Portal
# Otherwise, message.content will return empty
from discord import Intents
from discord.ext import commands

# Enable all standard intents and message content
# (prefix commands generally require message content)
intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


current_time = datetime.datetime.now()
timestamp = current_time.strftime("[%Y-%m-%d %H:%M:%S]")

# Event listener for when the bot has switched from offline to online
@bot.event
async def on_ready():
	# Creates a counter to keep track of how many guilds/servers the bot is connected to
	guild_count = 0

	# Loops through all the guild/servers that the bot is associated with
	for guild in bot.guilds:
		#Print the server's ID and name
		print(f"- {guild.id} (name: {guild.name})")

		# Increments the guild counter
		guild_count = guild_count + 1

	print("PARM is currently located in " + str(guild_count) + " guilds.")
	print(f"PARM's current permissions integer is {permissions_integer}")

# Event listened for when a new message is sent to a channel or DM
@bot.event
async def on_message(message):
	print(f"{timestamp} Received message: {message.content} in channel: {message.channel} from {message.author}")

	if message.content == "hello":
		
		print("Responding to hello message")
		# sends back a message to the channel (or DM)
		await message.channel.send("hey dirtbag")

# Executes the bot with the token defined in .env
bot.run(DISCORD_TOKEN)