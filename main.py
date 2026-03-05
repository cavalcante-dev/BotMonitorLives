from app.services.youtube_services import YoutubeServices
from app.config.settings import Settings

def main():
    youtube = YoutubeServices()
    response = youtube.buscarLive(Settings.channelId, "news")
    if response==True:
        print("Deu certo")
    else: 
        print("Deu errado") 

main()