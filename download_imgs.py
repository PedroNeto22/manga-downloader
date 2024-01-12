from get_urls_names import GetCapsUrls
import requests
import os
from urllib.parse import urlparse
import time


class Download:

    def __init__(self) -> None:
        pass

    def download_imgs(self, urls: list[str], cap_name: str, manga_name: str = 'manga'):

        manga_path = self.__create_manga_path(manga_name)

        cap_path = self.__create_cap_path(cap_name, str(manga_path))

        for url in urls:

            request = requests.get(url, stream=True)

            if request.status_code == 200:
                try:
                    file_name = cap_path+self.__get_file_name(url)
                    with open(file_name, 'wb') as f:
                        f.write(request.content)
                    time.sleep(5)
                except Exception as e:
                    print(f'Error: {e}')
                    return

    def __get_file_name(self, url: str):

        parsed_url = urlparse(url)

        file_name = os.path.basename(parsed_url.path)

        new_file_name = os.path.splitext(file_name)[0] + ".png"

        return new_file_name

    def __create_manga_path(self, manga_name: str):

        manga_path = './' + manga_name + '/'

        if not os.path.exists(manga_path):
            os.mkdir(manga_path)
            return manga_path

        return manga_path

    def __create_cap_path(self, cap_name: str, manga_path: str):

        cap_path = manga_path + cap_name + '/'

        if not os.path.exists(cap_path):
            os.mkdir(cap_path)
            return cap_path

        return cap_path


if __name__ == '__main__':
    teste = GetCapsUrls(
        'https://gekkou.site/manga/343599e3-2867-42cb-8439-7acede3ce775/')

    caps_urls = teste.get_caps_url_and_name()

    manga_name = str(teste.manga_name)

    download = Download()

    for cap in range(-1, -3, -1):
        cap_name = caps_urls[cap]['name']
        imgs_urls = teste.get_images_url(caps_urls[cap]['url'])
        download.download_imgs(imgs_urls, cap_name, manga_name)
