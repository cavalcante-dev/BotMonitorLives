# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import googleapiclient.discovery
import googleapiclient.errors
import re
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')
CHANNEL_ID = os.getenv('TARGET_CHANNEL_ID')

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def iniciar_youtube():
    api_key = os.getenv('YOUTUBE_API_KEY')
    if not api_key:
        raise ValueError("A chave da API não foi encontrada. Defina YOUTUBE_API_KEY como variável de ambiente.")

    youtube = build(serviceName='youtube', version='v3', developerKey=api_key)
    return youtube

def main():
    youtube = iniciar_youtube()
    request = youtube.search().list(
        part="snippet",
        channelId=CHANNEL_ID,
        eventType="live",
        maxResults=25,
        q="news",
        type="video"
    )
    response = request.execute()

    print(response)

