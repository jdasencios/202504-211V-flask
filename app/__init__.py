from flask import Flask

from app.config import Config
from app.db.database import close_db_connection
from app.routes.base_routes import base_bp
from app.routes.comment_routes import comments_bp
from app.routes.post_routes import post_bp
from app.routes.user_routes import users_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.teardown_appcontext(close_db_connection)

    app.register_blueprint(base_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(comments_bp)
    app.register_blueprint(users_bp)

    return app
