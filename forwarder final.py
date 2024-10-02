from pyrogram import Client
from pyrogram.errors import FloodWait
import time
from tqdm import tqdm

# Add your credentials here
api_id = 12862156  # Replace with your actual API ID
api_hash = 'd913a2ef10183c683144ff851481d9fd'  # Replace with your actual API Hash
phone_number = '+919150368665'  # Your phone number linked to the Telegram account

# Source and destination channel usernames (private channels)
source_channel = '@mr890189'  # Replace with your source private channel
destination_channel = '-1002250470922'  # Replace with your destination private channel

# Initialize the client
app = Client("user_session", api_id, api_hash, phone_number=phone_number)

def forward_old_messages():
    with app:
        messages = []

        # Get all messages from the source channel in chronological order
        for message in app.get_chat_history(source_channel, limit=None):
            messages.append(message)

        # Total number of messages to forward
        total_messages = len(messages)
        print(f"Total messages to forward: {total_messages}")

        # Reverse the messages to forward from oldest to newest
        messages.reverse()

        # Create a progress bar
        with tqdm(total=total_messages, desc="Forwarding Messages", unit="msg") as pbar:
            # Iterate over the messages in batches of 100
            for i in range(0, total_messages, 100):
                batch = messages[i:i + 100]  # Get the next batch of 100 messages
                
                # Forward messages in the correct order (oldest to newest)
                for message in batch:
                    try:
                        # Check the type of message and forward accordingly
                        if message.text:  # If it's a text message
                            app.send_message(destination_channel, message.text, reply_to_message_id=message.id)
                        elif message.photo:  # If it's a photo
                            app.send_photo(destination_channel, message.photo.file_id, caption=message.caption)
                        elif message.video:  # If it's a video
                            app.send_video(destination_channel, message.video.file_id, caption=message.caption)
                        elif message.document:  # If it's a document
                            app.send_document(destination_channel, message.document.file_id, caption=message.caption)

                        pbar.update(1)  # Update the progress bar
                    except FloodWait as e:
                        print(f"Rate limited. Waiting for {e.x} seconds.")
                        time.sleep(e.x)  # Wait for the specified duration
                    except Exception as e:
                        print(f"Failed to forward message: {e}")

                # Sleep for 30 seconds after forwarding a batch
                time.sleep(30)

# Start the bot
if __name__ == "__main__":
    forward_old_messages()
