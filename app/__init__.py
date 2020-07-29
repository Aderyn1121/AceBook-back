import os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
# from .aws3 import upload_file_to_s3
from app.routes import api
from app.models import db
from app.config import Configuration

# if os.environ.get("FLASK_ENV") == 'production':
#     app = Flask(__name__, static_folder='../acebook-frontend/build/static',
#                 static_url_path='/static')
# else:
app = Flask(__name__)

CORS(app)
app.config.from_object(Configuration)

db.init_app(app)
Migrate(app, db)

app.register_blueprint(api.api)


@app.route("/")
def home():
    return "Hello World!"

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     print(f'caught_path: {path}')
#     path_dir = os.path.abspath("./acebook-frontend/build")  # path react build
#     # If we make a request to /static/<some-file-path> for a directory that exists in
#     # our static build folder, serve that file
#     # This could be useful if we have images, audio, etc., that we want to have
#     # available as static resources
#     if path and os.path.exists(f'./acebook-frontend/build/static/{path}'):
#         return send_from_directory(os.path.join(path_dir), path)
#     # Otherwise, serve up the index.html. Our React router will handle any other routes
#     else:
#         return send_from_directory(os.path.join(path_dir), 'index.html')
