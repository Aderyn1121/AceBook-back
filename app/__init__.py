import os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from app.routes import api
from app.models.models import db
from app.config import Configuration

app = Flask(__name__)
CORS(app)
app.config.from_object(Configuration)

db.init_app(app)
Migrate(app, db)

app.register_blueprint(api.bp)