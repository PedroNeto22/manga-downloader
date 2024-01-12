from get_urls_names import GetCapsUrls
from download_imgs import Download
import sys


def initialize():

    teste = GetCapsUrls(input('Url da pagina do manga: '))
    print('-' * 25)
    print('Aguarde o carregamento')
    print('-' * 25)

    caps_urls = teste.get_caps_url_and_name()

    num_available_chapters = len(caps_urls)

    print('-' * 25)
    print('Carregamento concluído')
    print('-' * 25)

    for idx, cap_num in enumerate(caps_urls):
        print(f'[{idx+1}] - [{cap_num["name"]}]')

    print(f'Quantidade de capítulos disponíveis: {num_available_chapters}')

    manga_name = str(teste.manga_name)

    download = Download()

    inicial, final = get_caps_to_download(num_available_chapters)

    caps_to_download = range(inicial-1, final+1)

    for cap in caps_to_download:
        cap_name = caps_urls[cap]['name']
        print(f'Baixando o {cap_name}')
        imgs_urls = teste.get_images_url(caps_urls[cap]['url'])
        download.download_imgs(imgs_urls, cap_name, manga_name)


def get_caps_to_download(tamanho: int):

    try:
        inicial = int(input('Baixar do capitulo: '))
        final = int(input('Ate o capitulo: '))
        if (inicial > tamanho) or (final > tamanho) or (inicial > final) or (inicial < 0) or (final < 0):
            print('Índice do manga errado, encerrando programa')
            sys.exit()
        return inicial, final
    except:
        print('Formando errado, encerrando programa')
        sys.exit()


initialize()
