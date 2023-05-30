from flask import Blueprint, request, abort
from scrapers.televes_scraper import TelevesScraper
from managers.SeleniumManager import SeleniumManager

televes_bp = Blueprint("televes", __name__)


@televes_bp.route("/<product_id>")
def televes(product_id):
    """
    Route to scap information about the products in the caiado Website.

    Go to /televes/<id> to get the information about a product, where the <id> is the ID of the internal
    reference of the product in the store.

    Args:
        product_id: Internal ID of the product in the store to search for.

    Returns:
        JSON with the information of the product if was found.
        If the product was not found returns a simple page.
    """

    selenium_manager = SeleniumManager()

    reset_data_source = request.args.get("resetDataSource", default="False")

    if reset_data_source.lower() == "true":
        reset_data_source = True
    else:
        reset_data_source = False

    televes_scraper = TelevesScraper(selenium_manager.get_driver())

    print(f"Getting JSL product info for ID {product_id} ...")
    result = televes_scraper.scrape_product_info(product_id, reset_data_source)

    if result is not None:
        print(f"JSL product with ID {product_id} found")
        return result.to_json()
    else:
        print(f"JSL product with ID {product_id} not found!")
        abort(404, "Product not found")
