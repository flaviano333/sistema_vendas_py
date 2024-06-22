from flask import Flask
from app.config import DevelopmentConfig
from app.extensions import db
from app.models import Usuario, Perfil, Produto, Estoque, Categoria, Pagamento, Compra, Menu, Imagem, Desconto, DescontoProduto, ItemCarrinho, MenuHasPerfil

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
