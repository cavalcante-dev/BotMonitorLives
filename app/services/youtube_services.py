from googleapiclient.discovery import build
from app.config.settings import Settings

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

class YoutubeServices: 

    def __init__(self):
        self.youtube = build(
            serviceName='youtube', 
            version='v3', 
            developerKey=Settings.apiKey
        )   

    def buscarLive(self, channelId, query):
        request = self.youtube.search().list(
            part="snippet",
            channelId=channelId,
            eventType="live",
            maxResults=25,
            q=query,
            type="video"
        )
        request.execute()
        if request!=None:
            return True
        else: 
            return False
