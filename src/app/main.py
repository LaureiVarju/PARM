
from mangum import Mangum
from asgiref.wsgi import WsgiToAsgi

from flask import Flask, jsonify, request
from discord_interactions import verify_key_decorator

# Syntax to populate discord_token when running locally and reading from a .env file
# Import load_dotenv function from dotenv module.
import os
from dotenv import load_dotenv
# Loads the .env file that resides on the same level as the script.
load_dotenv()
# Grab the API token from the .env file.
DISCORD_PUBLIC_KEY = os.getenv("DISCORD_PUBLIC_KEY")


app = Flask(__name__)
asgi_app = WsgiToAsgi(app)
handler = Mangum(asgi_app)

@app.route("/", methods=["POST"])
async def interactions():
	print(f"Request: {request.json}")
	raw_request = request.json
	return interact(raw_request)

@verify_key_decorator(DISCORD_PUBLIC_KEY)
def interact(raw_request):
    if raw_request["type"] == 1:  # ping
        response_data = {"type": 1}  # pongp
    else:
        data = raw_request["data"]
        command_name = data["name"]
        
        if command_name == "hello":
            message_content = "Hello there!"

        response_data = {
            "type": 4,
            "data": {"content": message_content},
        }

    return jsonify(response_data)


if __name__ == "__main__":
	app.run(debug = True)