from flask import Blueprint, jsonify

error_handlers_bp = Blueprint("error_handlers", __name__)


@error_handlers_bp.app_errorhandler(404)
def handle_404(error):
    """
    Handle the Flask 404 error.

    Args:
        error: Error information.

    Returns:
        404 error JSON format.
    """
    response = {
        "error_code": 404,
        "error": error.description
    }
    return jsonify(response), 404
