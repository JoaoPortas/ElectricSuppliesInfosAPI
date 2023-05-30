from flask import Blueprint, request, abort
from scrapers.al_scraper import ALScraper
from managers.SeleniumManager import SeleniumManager

al_bp = Blueprint("al", __name__)


@al_bp.route("/<product_id>")
def efapel(product_id):
    """
    Route to scap information about the products in the caiado Website.

    Go to /efapel/<id> to get the information about a product, where the <id> is the ID of the internal
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

    efapel_scraper = ALScraper(selenium_manager.get_driver())

    print(f"Getting AL product info for ID {product_id} ...")
    result = efapel_scraper.scrape_product_info(product_id, reset_data_source)

    if result is not None:
        print(f"AL product with ID {product_id} found")
        return result.to_json()
    else:
        print(f"AL product with ID {product_id} not found!")
        abort(404, "Product not found")
