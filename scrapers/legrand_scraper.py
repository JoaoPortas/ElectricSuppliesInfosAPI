import urllib.request
import os
import pandas as pd
from selenium.webdriver.common.by import By
from models.product_info import ProductInfo


class LegrandScraper:
    """
    Allows to scrap information about the products for the Legrand brand.
    """
    def __init__(self, driver):
        """
        Initialize the webscraping tool.

        Args:
            driver: Driver from selenium to be used in the webscraping.
        """
        self.driver = driver

    def scrape_product_info(self, product_id, reset_data_source):
        """
        Scraps the product information from legrand official website exel.

        Args:
            reset_data_source: Boolean type, if true download again the datasource.
                If false uses the existing datasource.
            product_id: ID of the product to get the information.

        Returns:
            If succeeded, returns an object of ProductInfo type with the information of the products.
            If the product doesn't exist returns None.
        """

        filename = "downloads/legrand/legrand.xlsx"

        if reset_data_source or not os.path.exists(filename):
            self.driver.get("https://www.legrand.pt/index.php/documentacao/category/3-tabelas-de-precos")

            download_link = self.driver.find_element(By.XPATH, "//div[@class='pd-filename'][1]//div[1]//a")

            download_url = download_link.get_attribute("href")

            os.makedirs(os.path.dirname(filename), exist_ok=True)

            urllib.request.urlretrieve(download_url, filename)

        data_frame = pd.read_excel(filename)

        product_search = data_frame[data_frame.iloc[:, 0].str.lower() == str(product_id).lower()]

        if not product_search.empty:
            product_info = ProductInfo(
                str(product_search.iloc[0, 0]),
                str(product_search.iloc[0, 2]),
                str(product_search.iloc[0, 1]),
            )

            return product_info
        else:
            return None
