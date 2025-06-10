from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from . import base_views
    app.register_blueprint(base_views.bp)

    return app
