# Telegram Message Forwarder

This script allows you to forward messages from one Telegram channel to another. It supports forwarding text messages, photos, videos, and documents using the Pyrogram library to interact with the Telegram API.

## Features
- Forwards text messages, photos, videos, and documents.
- Supports both private and public channels.
- Implements rate limiting to prevent flooding.

## Requirements
- Python 3.7 or higher
- Pyrogram$
- TgCrypto (for better performance)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Er3n-Yeager/Telegram-channel-cloner.git
   cd telegram-message-forwarder
2. **Create virtual environment***
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
3. ***Install the required libraries***
   ```bash
   pip install pyrogram tgcrypto tqdm
4. ***Add Your Credentials***
   ```bash
   api_id = 'YOUR_API_ID'          # Replace with your actual API ID
   api_hash = 'YOUR_API_HASH'      # Replace with your actual API Hash
   phone_number = 'YOUR_PHONE'     # Your phone number linked to the Telegram account-international format
   source_channel = 'SOURCE_CHANNEL'  # Replace with your source channel
   destination_channel = 'DEST_CHANNEL'  # Replace with your destination channel
5. ***Run the script***
   ```bash
   python eren_cloner.py



 
