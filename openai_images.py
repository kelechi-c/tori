import os
from tqdm.auto import tqdm
from selenium.webdriver.common.by import By
from scraper_utils import download_element, init_driver


class OpenAIImageScraper:
    def __init__(self) -> None:
        self.openlink = "https://openai.com/"
        self.driver = init_driver(self.openlink)
        self.image_folder = "openai_illustrations"
        self.image_class = "img.object-cover.object-center"

        if os.path.exists is not True:
            os.mkdir(self.image_folder)

    def _get_image_links(self):
        try:
            card_elems = self.driver.find_elements(
                By.CSS_SELECTOR, self.image_class)

            imlinks = [card.get_attribute("src") for card in tqdm(card_elems)]
            print(f"found {len(imlinks)} links")
            self.driver.quit()

            return imlinks
        except Exception as e:
            print(e)

    def download_images(self):
        k = 0
        link_list = self._get_image_links()

        for file_link in tqdm(link_list):
            download_element(file_link, k, self.image_folder)
            k += 1

        print(f"{k} images downloaded from openAI site 🍻")


scraper = OpenAIImageScraper()
scraper.download_images()
