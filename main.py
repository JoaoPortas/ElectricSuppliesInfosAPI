from flask import Flask
from routes import *


app = Flask(__name__)

app.register_blueprint(error_handlers_bp)
app.register_blueprint(legrand_bp, url_prefix="/legrand")
app.register_blueprint(efapel_bp, url_prefix="/efapel")
app.register_blueprint(abb_bp, url_prefix="/abb")
app.register_blueprint(al_bp, url_prefix="/al")
app.register_blueprint(fermax_bp, url_prefix="/fermax")
app.register_blueprint(gewiss_bp, url_prefix="/gewiss")
app.register_blueprint(hager_bp, url_prefix="/hager")


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
