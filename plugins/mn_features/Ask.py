import requests
from MangoSeed import Mseed
from info import DATABASE_URI
from pyrogram import Client, filters

mongo_url = DATABASE_URI

@Client.on_message(filters.command("ask"))
async def ask(client, message):
    text = " ".join(message.command[1:])
    if len(message.command) < 2:
        return await message.reply_text("Please provide a query!")
    
    if message.reply_to_message:
        query = f"Old conversation: {message.reply_to_message.text}\nNew Conversation: {text}"
    else:
        query = text

    mes = await message.reply_text("🔍")
    k = Mseed(mongo_url)

    try:
        response = k.generate(
            system="You are Malayalam talking assistant, you only talk malayalam you act like a malayalam talking assistant.Your name is Mr.Been . Your owner is Albert @aktelegram1.You are a stern person. Your developer is Albert.For Telegram, contact him at @aktelegram1. Owned by @aktelegram1.Albert GitHub: https://github.com/mallu-movie-world-dev1 ",
            prompt=query,
            user_id=message.from_user.id,
            model="gpt-3.5"
        )
        content = response['result']
        await mes.edit(f"Hey {message.from_user.mention},\n\nQuery: {text}\n\nResult:\n\n{content}")

    except requests.exceptions.RequestException as e:
        error_message = f"Error making request: {str(e)}"[:100] + "...\n use /bug comment"
        await mes.edit(error_message)
    except Exception as e:
        error_message = f"Unknown error: {str(e)}"[:100] + "...\n use /bug comment"
        await mes.edit(error_message)
