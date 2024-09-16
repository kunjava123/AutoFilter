
import requests
import time
import os
from pyrogram import filters, Client

# Command handler for /gen
@Client.on_message(filters.command(['imagine', 'generate', 'gen']))
async def generate_image(client, message):
    # Get the prompt from the command
    prompt = ' '.join(message.command[1:])

    # Send a message to inform the user to wait
    wait_message = await message.reply_text("Please wait while I generate the image...")
    StartTime = time.time()

    # API endpoint URL
    url = 'https://img-gen.hazex.workers.dev/'

    # Form data for the request
    params = {
        'prompt': prompt,
        'improve': 'true',
        'imageCount': '1',
        'format': 'wide'
    }

    # Send a GET request to the API
    response = requests.get(url, params=params)

    if response.status_code == 200:
        try:
            if response.content:
                destination_dir = ''
                destination_path = os.path.join(destination_dir, 'generated_image.jpg')

                # Save the image to the destination path
                with open(destination_path, 'wb') as f:
                    f.write(response.content)

                # Delete the wait message
                await wait_message.delete()

                # Send the generated image
                await message.reply_photo(destination_path, caption=f"Here's the generated image!\nTime Taken: {time.time() - StartTime}")

                # Delete the generated image after sending
                os.remove(destination_path)
            else:
                await wait_message.edit_text("Failed to generate the image.")
        except Exception as e:
            await wait_message.edit_text("Error: {}".format(e))
    else:
        await wait_message.edit_text("Error: {}".format(response.status_code))
