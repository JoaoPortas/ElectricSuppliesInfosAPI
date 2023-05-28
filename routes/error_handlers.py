from flask import Blueprint, jsonify

error_handlers_bp = Blueprint("error_handlers", __name__)


@error_handlers_bp.app_errorhandler(404)
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
