from flask import Flask, render_template
import os
import sys
from app.home import home as home_blueprint


def init_extensions(app: Flask):
    # use .init_app() on your extensions to register them on
    # the Flask instance
    pass


def create_app(config_object_name) -> Flask:

    base_dir = '.'
    if hasattr(sys, '_MEIPASS'):
        base_dir = os.path.join(sys._MEIPASS)

    # Initialize the core application
    app = Flask(__name__, instance_relative_config=False,
                static_folder=os.path.join(base_dir, 'static'),
                template_folder=os.path.join(base_dir, 'templates'))
    app.config.from_object(config_object_name)

    # Initialize Plugins at startup using init_app()
    init_extensions(app)

    with app.app_context():
        app.register_blueprint(home_blueprint, url_prefix='/')

        @app.errorhandler(404)
        def page_not_found(error):
            return render_template('page/errors/404.html', title='Page Not Found'), 404

        return app
