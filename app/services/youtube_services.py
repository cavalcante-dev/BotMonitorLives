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
        response = request.execute()

        lives_encontradas = []

        items = response.get("items", [])

        if not items:
            print("Nenhuma live encontrada!")
            return []

        for item in items:
            video_id = item["id"]["videoId"]
            lives_encontradas.append(video_id)

        return lives_encontradas
