from app.extensions import db
from datetime import date

class Estoque(db.Model):
    __tablename__ = 'estoque'
    idestoque = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantidade = db.Column(db.Integer, nullable=False)
    data_criacao = db.Column(db.Date, nullable=False, default=date.today)
    data_modificado = db.Column(db.Date, nullable=False, default=date.today)

class Categoria(db.Model):
    __tablename__ = 'categoria'
    idcatergoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_categoria = db.Column(db.String(45), nullable=False)
    descricao = db.Column(db.String(150), nullable=False)

class Produto(db.Model):
    __tablename__ = 'produto'
    idproduto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_produto = db.Column(db.String(45), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    link_download = db.Column(db.String(100), unique=True)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    idestoque = db.Column(db.Integer, db.ForeignKey('estoque.idestoque'), nullable=False)
    categoria_idcatergoria = db.Column(db.Integer, db.ForeignKey('categoria.idcatergoria'), nullable=False)

    estoque = db.relationship('Estoque')
    categoria = db.relationship('Categoria')

class Pagamento(db.Model):
    __tablename__ = 'pagamento'
    idpagamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(45), nullable=False)
    status = db.Column(db.Boolean, nullable=False)

class Compra(db.Model):
    __tablename__ = 'compra'
    idcompra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor_total = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(45), nullable=False)
    data_criacao = db.Column(db.Date, nullable=False, default=date.today)
    descricao = db.Column(db.String(100), nullable=False)
    idpagamento = db.Column(db.Integer, db.ForeignKey('pagamento.idpagamento'), nullable=False)

    pagamento = db.relationship('Pagamento')

class Menu(db.Model):
    __tablename__ = 'menu'
    idmenu = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu = db.Column(db.String(45), nullable=False)
    link = db.Column(db.String(100), nullable=False)

class Perfil(db.Model):
    __tablename__ = 'perfil'
    idperfil = db.Column(db.Integer, primary_key=True, autoincrement=True)
    perfil = db.Column(db.String(45), nullable=False)

class Imagem(db.Model):
    __tablename__ = 'imagem'
    idimagem = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(45), nullable=False)
    caminho = db.Column(db.String(100), nullable=False)
    data_criacao = db.Column(db.Date, nullable=False, default=date.today)
    data_modificado = db.Column(db.Date, nullable=False, default=date.today)
    idproduto = db.Column(db.Integer, db.ForeignKey('produto.idproduto'), nullable=False)

    produto = db.relationship('Produto')

class Desconto(db.Model):
    __tablename__ = 'desconto'
    id_desconto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(45))
    porcentagem = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.Boolean, nullable=False)

class DescontoProduto(db.Model):
    __tablename__ = 'desconto_produto'
    desconto_id_desconto = db.Column(db.Integer, db.ForeignKey('desconto.id_desconto'), primary_key=True)
    produto_idproduto = db.Column(db.Integer, db.ForeignKey('produto.idproduto'), primary_key=True)

    desconto = db.relationship('Desconto')
    produto = db.relationship('Produto')

class Usuario(db.Model):
    __tablename__ = 'usuario'
    idusuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(45), nullable=False)
    login = db.Column(db.String(20), nullable=False, unique=True)
    senha = db.Column(db.String(45), nullable=False)
    celular = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    status = db.Column(db.Boolean, nullable=False)
    data_criacao = db.Column(db.Date, nullable=False, default=date.today)
    data_modificado = db.Column(db.Date, nullable=False, default=date.today)
    perfil_idperfil = db.Column(db.Integer, db.ForeignKey('perfil.idperfil'), nullable=False)

    perfil = db.relationship('Perfil')

class ItemCarrinho(db.Model):
    __tablename__ = 'item_carrinho'
    idproduto = db.Column(db.Integer, db.ForeignKey('produto.idproduto'), primary_key=True)
    idusuario = db.Column(db.Integer, db.ForeignKey('usuario.idusuario'), primary_key=True)
    idcompra = db.Column(db.Integer, db.ForeignKey('compra.idcompra'), primary_key=True)

    produto = db.relationship('Produto')
    usuario = db.relationship('Usuario')
    compra = db.relationship('Compra')

class MenuHasPerfil(db.Model):
    __tablename__ = 'menu_has_perfil'
    menu_idmenu = db.Column(db.Integer, db.ForeignKey('menu.idmenu'), primary_key=True)
    perfil_idperfil = db.Column(db.Integer, db.ForeignKey('perfil.idperfil'), primary key=True)

    menu = db.relationship('Menu')
    perfil = db.relationship('Perfil')
