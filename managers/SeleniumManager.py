from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumManager:
    """
    Manages the selenium instance.

    Manages the selenium instance using a Singleton pattern.
    """
    _instance = None

    def __init__(self):
        self.driver = None
        if SeleniumManager._instance is None:
            self.setup_driver()
            print("no instance yet")
        else:
            self.driver = SeleniumManager._instance
            print("already exists")

    def setup_driver(self):
        """
        Setups the driver to be used by selenium, currently using Chrome.
        """
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        if SeleniumManager._instance is None:
            SeleniumManager._instance = self.driver

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
