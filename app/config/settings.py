import os
from dotenv import load_dotenv

load_dotenv()

class Settings: 
    
    apiKey = os.getenv("YOUTUBE_API_KEY")
    channelId = os.getenv("TARGET_CHANNEL_ID")
    whatsappNumber = os.getenv("WHASTAPP_NUMBER")

    