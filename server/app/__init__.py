from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_dotenv import DotEnv
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize dotenv to load environment variables from .env
    env = DotEnv(app)
    env.init_app(app, verbose_mode=True)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    from app.routes.usuario_routes import bp as usuario_bp
    app.register_blueprint(usuario_bp)

    from app.routes.produto_routes import bp as produto_bp
    app.register_blueprint(produto_bp)

    return app
