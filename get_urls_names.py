from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class GetCapsUrls:

    def __init__(self, url: str) -> None:

        self._url = url

        self.manga_name = None

        # self._list_of_links = None

    def get_caps_url_and_name(self) -> list[dict[str, str]]:

        option = Options()

        option.add_argument("--headless=new")

        driver = webdriver.Chrome(options=option)

        driver.get(self._url)

        time.sleep(5)

        self.manga_name = driver.find_element(
            By.CSS_SELECTOR, '#manga-title h1').text

        btn_show = driver.find_element(
            By.XPATH, '//*[@id="manga-chapters-holder"]/div/div/div/span')

        btn_show.click()

        elements = driver.find_elements(By.CLASS_NAME, 'wp-manga-chapter')

        filtered_elements = [element.find_element(
            By.CSS_SELECTOR, 'a') for element in elements]

        list_of_links = [{"name": str(link.text).strip(), "url": str(link.get_attribute(
            'href')).strip()} for link in filtered_elements]

        driver.quit()

        list_of_links = sorted(
            list_of_links, key=lambda x: int(x['name'][9:]))

        return list_of_links

    def get_images_url(self, url: str):

        option = Options()

        option.add_argument("--headless=new")

        driver = webdriver.Chrome(options=option)

        driver.get(url)

        images = driver.find_elements(By.CLASS_NAME, 'wp-manga-chapter-img')

        images_links = [str(link.get_attribute('data-src')).strip()
                        for link in images]

        return images_links


if __name__ == '__main__':

    urls = GetCapsUrls(
        'https://gekkou.site/manga/83150c8e-4f7b-4d4e-bd38-f333bfdabb45/')

    caps_urls = urls.get_caps_url_and_name()

    for url in caps_urls:
        print(url)
    print(len(caps_urls))
    print(urls.manga_name)
