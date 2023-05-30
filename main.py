from flask import Flask
from routes.error_handlers import error_handlers_bp
from routes.legrand_routes import legrand_bp
from routes.efapel_routes import efapel_bp
from routes.abb_routes import abb_bp
from routes.al_routes import al_bp

app = Flask(__name__)

app.register_blueprint(error_handlers_bp)
app.register_blueprint(legrand_bp, url_prefix="/legrand")
app.register_blueprint(efapel_bp, url_prefix="/efapel")
app.register_blueprint(abb_bp, url_prefix="/abb")
app.register_blueprint(al_bp, url_prefix="/al")


@app.route("/")
def hello_world():
    """
    Just a simple hello world test!

    The root page with a simple hello world.

    Returns:
        page: A page with hello world!
    """
    return "<h1>Hello, World!</h1>"


if __name__ == "__main__":
    app.run()
