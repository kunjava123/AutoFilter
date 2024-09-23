
from pyrogram import Client, filters
import httpx
import asyncio

# Define the API URL and the role as constants
API_URL = "https://horridapi2-0.onrender.com/ai?model=5"
ASSISTANT_ROLE = """You are a helpful assistant. 
                    Your name is Mohanlal . Your owner is MN TG @mntgxo. 
                    Your developer is MN TG. 
                    For Telegram, contact him at @mntgxo. Owned by @mntgxo"""

@Client.on_message(filters.command(["gpt","gpt4"]))
async def modelai_command(client, message):
    # Check if the command has a query
    if len(message.command) < 2:
        await message.reply_text("Please provide a query")
        return

    # Extract the query from the command
    query = " ".join(message.command[1:])

    # Define the payload for the API request
    payload = {
        "messages": [
            {
                "role": "assistant",
                "content": ASSISTANT_ROLE
            }, 
            {
                "role": "user", 
                "content": query
            }
        ]  
    }

    try:
        # Make the API request using httpx
        async with httpx.AsyncClient() as client:
            response = await client.post(API_URL, json=payload)
            response_json = response.json()

        # Extract the response from the API
        response_text = "ʜᴇʏ: " + message.from_user.mention + "\n\nϙᴜᴇʀʏ: " + query + "\n\nʀᴇsᴜʟᴛ:\n" + response_json.get("response", "No response from the AI")
        await message.reply_text(response_text)
    except httpx.HTTPError as e:
        # Handle any HTTP errors that occur
        await message.reply_text(f"An error occurred: {e}")
