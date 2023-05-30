from flask import Blueprint, request, abort
from scrapers.tev2_scraper import TEV2Scraper
from managers.SeleniumManager import SeleniumManager

tev2_bp = Blueprint("tev2", __name__)


@tev2_bp.route("/<product_id>")
def jsl(product_id):
    """
    Route to scrap information about the products in the caiado Website.

    Go to /tev2/<id> to get the information about a product, where the <id> is the ID of the internal
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

    tev2_scraper = TEV2Scraper(selenium_manager.get_driver())

    print(f"Getting TEV2 product info for ID {product_id} ...")
    result = tev2_scraper.scrape_product_info(product_id, reset_data_source)

    if result is not None:
        print(f"TEV2 product with ID {product_id} found")
        return result.to_json()
    else:
        print(f"TEV2 product with ID {product_id} not found!")
        abort(404, "Product not found")
