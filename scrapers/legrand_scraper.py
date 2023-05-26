from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from models.product_info import ProductInfo


class LegrandScraper:
    """
    Allows to scrap information about the products for the Legrand website.
    """
    def __init__(self, driver):
        """
        Initialize the webscraping tool.

        Args:
            driver: Driver from selenium to be used in the webscraping.
        """
        self.driver = driver

    def scrape_product_info(self, product_id):
        """
        Scraps the product information.

        Args:
            product_id: ID of the product to get the information.

        Returns:
            If succeeded, returns an object of ProductInfo type with the information of the products.
            If the product doesn't exist returns None.
        """
        # Go to website and find the product
        self.driver.get(f"https://www.legrand.pt/e-catalogo/catalogsearch/result/?q={product_id}")

        # Get the product data

        try:
            title_element = self.driver.find_element(By.XPATH, "//div[@class='product-title']//div[2]//h1[1]//span[1]")
            price_element = self.driver.find_element(By.XPATH, "//table[@id='product-attribute-specs-table']//td[1]//span[1]")
        except NoSuchElementException:
            return None

        # Get the text from the elements
        title = title_element.text
        price = price_element.text

        product_info = ProductInfo(title, price)

        # Print the extracted info
        product_info.print_info()

        return product_info
