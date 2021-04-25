from flask import Flask


def create_app():
	app = Flask(__name__)

	from .controllers.home import home as home_blueprint
	app.register_blueprint(home_blueprint)

	return app
