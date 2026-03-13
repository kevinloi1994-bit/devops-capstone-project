from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    # Enable security headers
    Talisman(app)

    # Enable CORS
    CORS(app)

    return app
