import time
import re
import pywhatkit as kit
from app.services.youtube_services import YoutubeServices
from app.services.description_extractor import DescriptionExtractor
from app.config.settings import Settings

def extrair_link_presenca(descricao):
    if not descricao:
        return None

    padrao = r"📝 Registre sua presença na live: \s*(https?://[^\s]+)"
    resultado = re.search(padrao, descricao, re.IGNORECASE)

    if resultado:
        return resultado.group(1)
    return None

def enviar_mensagem(link):
    zapNumber = Settings.whatsappNumber;
    kit.sendwhatmsg_instantly(zapNumber,
                                f"Tome o link de presença: {link}" )

def main():
    print("Iniciando o Bot de Monitorização\n")

    youtube_services = YoutubeServices()
    extrator = DescriptionExtractor()

    video_ids = youtube_services.buscarLive(Settings.channelId, "news")

    if not video_ids:
        print("Nenhuma live encontrada no canal neste momento.")
        return
    
    lives_monitoradas = video_ids.copy()

    while len(lives_monitoradas) > 0:

        for video_id in lives_monitoradas[:]:

            descricao = extrator.obter_descricao_video(video_id)

            link = extrair_link_presenca(descricao)

            if link:
                print(f"Link encontrado na live {video_id}!")
                print(f"URL: {link}")

                lives_monitoradas.remove(video_id)
            else:
                print("Link ainda não está disponível.")

            enviar_mensagem(link)

        if len(lives_monitoradas) > 0:
            print("\nAguardando 60 segundos para a próxima verificação...\n")
            time.sleep(60)

    print("Monitorização concluída!")


if __name__ == "__main__":
    main()