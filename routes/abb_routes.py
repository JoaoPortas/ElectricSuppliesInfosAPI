from flask import Blueprint, request, abort
from scrapers.abb_scraper import ABBScraper
from managers.SeleniumManager import SeleniumManager

abb_bp = Blueprint("abb", __name__)


@abb_bp.route("/<product_id>")
def abb(product_id):
    """
    Route to scap information about the ABB products in the caiado Website.

    Go to /abb/<id> to get the information about a product, where the <id> is the ID of the internal
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

    abb_scraper = ABBScraper(selenium_manager.get_driver())

    print(f"Getting ABB product info for ID {product_id} ...")
    result = abb_scraper.scrape_product_info(product_id, reset_data_source)

    if result is not None:
        print(f"ABB product with ID {product_id} found")
        return result.to_json()
    else:
        print(f"ABB product with ID {product_id} not found!")
        abort(404, "Product not found")
