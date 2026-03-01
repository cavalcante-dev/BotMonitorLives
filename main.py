import os
import re
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')
CHANNEL_ID = os.getenv('TARGET_CHANNEL_ID')


def iniciar_youtube():
    api_key = os.getenv('YOUTUBE_API_KEY')
    if not api_key:
        raise ValueError("A chave da API não foi encontrada. Defina YOUTUBE_API_KEY como variável de ambiente.")

    youtube = build(serviceName='youtube', version='v3', developerKey=api_key)
    return youtube

def buscar_live(youtube, channel_id=None):
    request = youtube.search().list(
        part="snippet",
        eventType="live",
        type="video",
        channelId=channel_id
    )
    response = request.execute()
    if response.get("items"):
        return response
    else:
        print("Nenhuma live encontrada!!")
        return None
