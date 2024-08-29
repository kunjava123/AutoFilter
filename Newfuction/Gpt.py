from pyrogram import Client, filters
import httpx
import asyncio

@Client.on_message(filters.command(["gpt","gpt4"]))
async def modelai_command(client, message):
    if len(message.command) < 2:
        await message.reply_text("Please provide a query")
        return

    query = " ".join(message.command[1:])

    api = "https://horrid-api-yihb.onrender.com/ai?model=5"
    role = """You are a helpful assistant. 
              Your name is Minnal Murali . Your owner is MN TG @mntgxo. 
              Your developer is MN TG. 
              For Telegram, contact him at @mntgxo. Owned by @mntgxo"""

    payload = {
        "messages": [
            {
                "role": "assistant",
                "content": role
            }, 
            {
                "role": "user", 
                "content": query
            }
        ]  
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(api, json=payload)
        response_json = response.json()

    response_text = "ʜᴇʏ: " + message.from_user.mention + "\n\nϙᴜᴇʀʏ: " + query + "\n\nʀᴇsᴜʟᴛ:\n" + response_json.get("response", "No response from the AI")
    await message.reply_text(response_text)
