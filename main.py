from flask import Flask
from managers.SeleniumManager import SeleniumManager
from scrapers.selenium_scraper import SeleniumScraper
from scrapers.legrand_scraper import LegrandScraper

selenium_manager = SeleniumManager()
selenium_manager.setup_driver()

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    Just a simple hello world test!

    The root page with a simple hello world.

    Returns:
        page: A page with hello world!
    """
    return "<h1>Hello, World!</h1>"


@app.route("/selenium")
def selenium():
    """
    Tests the selenium in the app.

    To see if selenium is well configuration accessible by /selenium

    Returns:
        page: With the selenium scrapped data.
    """
    selenium_scraper = SeleniumScraper(selenium_manager.get_driver())
    result = selenium_scraper.scrape_website()
    # selenium_manager.close_driver()
    return f"<h1>Scraped title: {result}</h1>"


if __name__ == "__main__":
    app.run()
