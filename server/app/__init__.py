from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_dotenv import DotEnv
from config import Config
from app.extensions import db
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
    from app.routes.categoria_routes import bp as estoque_bp
    from app.routes.estoque_routes import bp as categoria_bp
    from app.routes.produto_routes import bp as produto_bp
    from app.routes.pagamento_routes import bp as pagamento_bp #daqui foi feito por IA
    from app.routes.compra_routes import bp as compra_bp
    from app.routes.menu_routes import bp as menu_bp
    from app.routes.imagem_routes import bp as imagem_bp
    from app.routes.desconto_routes import bp as desconto_bp
    from app.routes.descontoProduto_routes import bp as descontoProduto_bp
    from app.routes.itemCarrinho_routes import bp as itemCarrinho_bp
    from app.routes.menuHasPerfil_routes import bp as menuHasPerfil_bp
    from app.routes.perfil_routes import bp as perfil_bp

    app.register_blueprint(usuario_bp)
    app.register_blueprint(estoque_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(produto_bp)
    app.register_blueprint(pagamento_bp)
    app.register_blueprint(compra_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(imagem_bp)
    app.register_blueprint(desconto_bp)
    app.register_blueprint(descontoProduto_bp)
    app.register_blueprint(itemCarrinho_bp)
    app.register_blueprint(menuHasPerfil_bp)
    app.register_blueprint(perfil_bp)

    return app
