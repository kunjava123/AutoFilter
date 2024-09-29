import os
import base64
import requests
from pyrogram import Client, filters

# Define your message handler
@Client.on_message(filters.command('enhance'))
async def enhance(client, message):
    # Check if the command is replying to a message and if that message is a photo or sticker
    if message.reply_to_message and (message.reply_to_message.photo or message.reply_to_message.sticker):
        user_id = message.from_user.id
        reply = message.reply_to_message
        # Download the photo or sticker
        path = await reply.download(file_name=f"{user_id}.jpeg")
        # Inform user that the request is being processed
        msg = await message.reply_text("Wait a moment, we're processing your request.")
        
        with open(path, 'rb') as file:
            photo = file.read()
            
        # Encode the image data to base64
        encoded_image_data = base64.b64encode(photo).decode('utf-8')
        
        # Define API endpoint and headers
        url = 'https://apis-awesome-tofu.koyeb.app/api/remini?mode=enhance'
        headers = {'Content-Type': 'application/json'}
        
        # Prepare data for API request
        data = {"imageData": encoded_image_data}
        
        try:
            # Send POST request to the API
            response = requests.post(url, headers=headers, json=data)
            # Check if the request was successful
            if response.status_code == 200:
                # Inform user that the photo is being sent
                await msg.edit('✨ Almost done now... Sending photo... ❤️')
                # Save enhanced photo
                enhanced_path = f"enhanced_{user_id}.jpeg"
                with open(enhanced_path, 'wb') as file:
                    file.write(response.content)
                # Send the enhanced photo
                await message.reply_document(document=enhanced_path, quote=True)
                # Delete the temporary files and the processing message
                await msg.delete()
                os.remove(path)
                os.remove(enhanced_path)
            else:
                await message.reply_text(f"❌ Error occurred when processing: {response.text}")
        except Exception as e:
            await message.reply_text(f"❌ Error occurred when processing: {e}")
            # Log the exception for debugging
            print(f"Exception: {e}")
