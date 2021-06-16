"""
Running the 'create_app' function to compile the application
for Flask.
"""

from flask import Flask
from .app import DB

from .app import create_app
# def create_app():

APP = create_app()


# DATABASE_URL = "sqlite:///twitoff_27_dev.db" # Using relative filepath

# def create_app():
#     app = Flask(__name__)

#     app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#     DB.init_app(app)
#     migrate.init_app(app, DB)

#     app.register_blueprint(home_routes)
#     app.register_blueprint(book_routes)
#     return app

# if __name__ == "__main__":
#     my_app = create_app()
#     my_app.run(debug=True)