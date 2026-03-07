from app.config.settings import Settings
from googleapiclient.discovery import build
from app.services.youtube_services import YoutubeServices


class DescriptionExtractor:

    def __init__(self):
        self.youtube = build(
            serviceName='youtube',
            version='v3',
            developerKey=Settings.apiKey
        )

        self.youtube_services = YoutubeServices()

    def extrair_descricoes(self, channelId, query=""):
        video_ids = self.youtube_services.buscarLive(channelId, query)

        if len(video_ids) == 0:
            print("Nenhuma live acontecendo neste momento.")
            return []

        todas_as_descricoes = []

        for video_id in video_ids:
            request = self.youtube.videos().list(
                part="snippet",
                id=video_id
            )
            response = request.execute()

            if "items" in response and len(response["items"]) > 0:
                descricao = response["items"][0]["snippet"]["description"]

                dados_live = {
                    "id_video": video_id,
                    "descricao": descricao
                }
                todas_as_descricoes.append(dados_live)

                print(f"Descrição extraida com sucesso da live: {video_id}")

                return todas_as_descricoes
            else:
                print(f"Não foi possível extrair a descrição do vídeo {video_id}!")
                continue

        return todas_as_descricoes