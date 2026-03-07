from app.services.description_extractor import DescriptionExtractor
from app.config.settings import Settings


def main():
    print(f"Iniciando monitoramento no canal")

    extrator = DescriptionExtractor()

    lista_de_lives = extrator.extrair_descricoes(channelId=Settings.channelId, query="news")

    if len(lista_de_lives) > 0:
        print(f"\nDeu certo! live processada com sucesso.\n")
    else:
        print("\nNenhuma live encontrada ou não foi possível extrair os dados.")

if __name__ == "__main__":
    main()