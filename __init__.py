from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

Talisman(app)
CORS(app)
