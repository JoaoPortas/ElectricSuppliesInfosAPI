from flask import Flask, request, jsonify, abort
from managers.SeleniumManager import SeleniumManager
from scrapers.selenium_scraper import SeleniumScraper
from routes.legrand_routes import legrand_bp

app = Flask(__name__)

app.register_blueprint(legrand_bp, url_prefix="/legrand")


@app.route("/")
def hello_world():
    """
    Just a simple hello world test!

    The root page with a simple hello world.

    Returns:
        page: A page with hello world!
    """
    return "<h1>Hello, World!</h1>"


@app.errorhandler(404)
def handle_404(error):
    """
    Handle the Flask 404 error when a product is not found.

    Args:
        error: Error information.

    Returns:
        404 error min JSON format.
    """
    response = {
        "error": "Page not found",
        "message": error.description
    }
    return jsonify(response), 404


if __name__ == "__main__":
    app.run()
