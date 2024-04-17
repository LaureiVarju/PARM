import requests
import yaml
import os

from dotenv import load_dotenv
# Loads the .env file that resides on the same level as the script.
load_dotenv()
# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
APPLICATION_ID =os.getenv("APPLICATION_ID")
URL = f"https://discord.com/api/v9/applications/{APPLICATION_ID}/commands"

print(DISCORD_TOKEN)
print(APPLICATION_ID)
print(URL)


with open ("discord_commands.yaml", "r") as file:
	yaml_content = file.read()

commands = yaml.safe_load(yaml_content)
print(commands)
headers = {"Authorization": f"Bot {DISCORD_TOKEN}", "Content-Type": "application/json"}

#send the POST request for each command
for command in commands:
	response = requests.post(URL, json=command, headers=headers)
	command_name = command["name"]
	print(f"Command {command_name} created: {response.status_code}")

