class SeleniumScraper:
    def __init__(self, driver):
        self.driver = driver

    def scrape_website(self):
        self.driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        title = self.driver.title

        return title
