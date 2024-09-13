from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Mangandi import ImageUploader, VideoUploader

@Client.on_message(filters.command(["mangandi", "telegraph" "img2link", "manga", "ma","vid2link"]))
async def mangandi (client, message):
    if message.reply_to_message:
        if message.reply_to_message.photo:
            photo = message.reply_to_message.photo
            if photo.file_size > 500 * 1024 * 1024:  # 500 MB
                await message.reply("Image size is too large! Maximum allowed size is 500 MB")
                return
            k = await message.reply_to_message.download()
            up = ImageUploader(k)
            link = up.upload()
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("Share Link", url=f"https://telegram.me/share/url?url={link}"),
                 InlineKeyboardButton("Copy Link", url=f"{link}")]
            ])
            k = await message.reply_text("`Downloading To My Server ...`")
            await k.edit("`Downloading Completed. Now I am Uploading ...`")
            await k.edit(f"**Link: {link}**\n\n**Copy link:** `{link}`\n\n>**By: @mnbots**", reply_markup=keyboard)
        elif message.reply_to_message.video:
            video = message.reply_to_message.video
            if video.file_size > 500 * 1024 * 1024:  # 500 MB
                await message.reply("Video size is too large! Maximum allowed size is 500 MB")
                return
            k = await message.reply_to_message.download()
            up = VideoUploader(k)
            link = up.upload()
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("Share Link", url=f"https://telegram.me/share/url?url={link}"),
                 InlineKeyboardButton("Copy Link", url=f"{link}")]
            ])
            k = await message.reply_text("`Downloading To My Server ...`")
            await k.edit("`Downloading Completed. Now I am Uploading ...`")
            await k.edit(f"**Link: {link}**\n\n**Copy link:** `{link}`\n\n>**By: @mnbots**", reply_markup=keyboard)
        else:
            await message.reply("Please reply to a photo or video")
    else:
        await message.reply("Please reply to a photo or video")
