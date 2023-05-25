from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumManager:
    """
    Manages de selenium instance.

    Manges the selenium instance.
    """
    def __init__(self):
        """
        Initialize the driver of selenium as None.
        """
        self.driver = None

    def setup_driver(self):
        """
        Setups the driver to be used by selenium what is currently the chrome.
        """
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def get_driver(self):
        """
        Returns the current driver used by selenium.

        Returns:
            Driver used by selenium.
        """
        return self.driver

    def close_driver(self):
        """
        Closes the driver of the selenium.
        """
        self.driver.close()
