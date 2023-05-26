from flask import Flask, jsonify, abort
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


@app.route("/legrand/<int:product_id>")
def legrand(product_id):
    """
    Route to scap information about the products in the Legrand Website.

    Go to /legrand/<id> to get the information about a product, where the <id> is the ID of the internal
    reference of the product in the store.

    Args:
        product_id: Internal ID of the product in the store to search for.

    Returns:
        JSON with the information of the product if was found.
        If the product was not found returns a simple page.
    """
    legrand_scraper = LegrandScraper(selenium_manager.get_driver())

    print(f"Getting Legrand product info for ID {product_id} ...")
    result = legrand_scraper.scrape_product_info(product_id)

    if result != None:
        print(f"Legrand product with ID {product_id} found")
        return result.to_json()
    else:
        print(f"Legrand product with ID {product_id} not found!")
        abort(404, "Product not found")


@app.errorhandler(404)
def handle_404(error):
    response = {
        "error": "Page not found",
        "message": error.description
    }
    return jsonify(response), 404


if __name__ == "__main__":
    app.run()
