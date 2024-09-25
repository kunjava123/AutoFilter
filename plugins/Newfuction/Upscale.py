import base64
import httpx
import os
import requests 
from pyrogram import filters
from pyrogram import *
from pyrogram import filters
import pyrogram
from uuid import uuid4
from pyrogram.types import *


@Client.on_message(filters.command("upscale"))
async def upscale(client, message):
    try:
        if not message.reply_to_message or not message.reply_to_message.photo:
            await message.reply_text("**ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ᴛᴏ ᴜᴘsᴄᴀʟᴇ ɪᴛ.**")
            return

        k = await message.reply_text("wait few mint")
        image = message.reply_to_message.photo.file_id
        file_path = await client.download_media(image)

        with open(file_path, "rb") as image_file:
            f = image_file.read()

        b = base64.b64encode(f).decode("utf-8")

        async with httpx.AsyncClient() as http_client:
            response = await http_client.post(
                "https://api.qewertyy.dev/upscale", data={"image_data": b}, timeout=None
            )

        with open("upscaled.png", "wb") as output_file:
            output_file.write(response.content)

        await client.send_document(
            message.chat.id,
            document="upscaled.png",
            caption="**ʜᴇʀᴇ ɪs ᴛʜᴇ ᴜᴘsᴄᴀʟᴇᴅ ɪᴍᴀɢᴇ!**",
        )
        await k.delete()

    except Exception as e:
        print(f"**ғᴀɪʟᴇᴅ ᴛᴏ ᴜᴘsᴄᴀʟᴇ ᴛʜᴇ ɪᴍᴀɢᴇ**: {e}")
        await message.reply_text("**ғᴀɪʟᴇᴅ ᴛᴏ ᴜᴘsᴄᴀʟᴇ ᴛʜᴇ ɪᴍᴀɢᴇ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ**. {e}")
