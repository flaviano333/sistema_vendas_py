from app.extensions import db
from datetime import date

class Estoque(db.Model):
    __tablename__ = 'estoque'
    idestoque = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantidade = db.Column(db.Integer, nullable=False)
    data_criacao = db.Column(db.Date, nullable=False, default=date.today)
    data_modificado = db.Column(db.Date, nullable=False, default=date.today)
    def to_json(self):
        return {
            'idestoque': self.idestoque,
            'quantidade': self.quantidade,
            'data_criacao': self.data_criacao.isoformat(),
            'data_modificado': self.data_modificado.isoformat()
        }    

class Categoria(db.Model):
    __tablename__ = 'categoria'
    idcatergoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_categoria = db.Column(db.String(45), nullable=False)
    descricao = db.Column(db.String(150), nullable=False)
    def to_json(self):
        return {
            'idcatergoria': self.idcatergoria,
            'nome_categoria': self.nome_categoria,
            'descricao': self.descricao
        }    

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
    def to_json(self):
        return {
            'idproduto': self.idproduto,
            'nome_produto': self.nome_produto,
            'status': self.status,
            'link_download': self.link_download,
            'preco': str(self.preco),
            'idestoque': self.idestoque,
            'categoria_idcatergoria': self.categoria_idcatergoria
        }

class Pagamento(db.Model):
    __tablename__ = 'pagamento'
    idpagamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(45), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    def to_json(self):
        return {
            'idpagamento': self.idpagamento,
            'tipo': self.tipo,
            'status': self.status
        }
    
class Compra(db.Model):
    __tablename__ = 'compra'
    idcompra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor_total = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(45), nullable=False)
    data_criacao = db.Column(db.Date, nullable=False, default=date.today)
    descricao = db.Column(db.String(100), nullable=False)
    idpagamento = db.Column(db.Integer, db.ForeignKey('pagamento.idpagamento'), nullable=False)

    pagamento = db.relationship('Pagamento')
    def to_json(self):
        return {
            'idcompra': self.idcompra,
            'valor_total': str(self.valor_total),
            'status': self.status,
            'data_criacao': self.data_criacao.isoformat(),
            'descricao': self.descricao,
            'idpagamento': self.idpagamento
        }    

class Menu(db.Model):
    __tablename__ = 'menu'
    idmenu = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu = db.Column(db.String(45), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    def to_json(self):
        return {
            'idmenu': self.idmenu,
            'menu': self.menu,
            'link': self.link
        }
    
class Perfil(db.Model):
    __tablename__ = 'perfil'
    idperfil = db.Column(db.Integer, primary_key=True, autoincrement=True)
    perfil = db.Column(db.String(45), nullable=False)
    def to_json(self):
        return {
            'idperfil': self.idperfil,
            'perfil': self.perfil
        }
    
class Imagem(db.Model):
    __tablename__ = 'imagem'
    idimagem = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(45), nullable=False)
    caminho = db.Column(db.String(100), nullable=False)
    data_criacao = db.Column(db.Date, nullable=False, default=date.today)
    data_modificado = db.Column(db.Date, nullable=False, default=date.today)
    idproduto = db.Column(db.Integer, db.ForeignKey('produto.idproduto'), nullable=False)
    produto = db.relationship('Produto')
    def to_json(self):
        return {
            'idimagem': self.idimagem,
            'nome': self.nome,
            'caminho': self.caminho,
            'data_criacao': self.data_criacao.isoformat(),
            'data_modificado': self.data_modificado.isoformat(),
            'idproduto': self.idproduto
        }    

class Desconto(db.Model):
    __tablename__ = 'desconto'
    id_desconto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(45))
    porcentagem = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    def to_json(self):
        return {
            'id_desconto': self.id_desconto,
            'descricao': self.descricao,
            'porcentagem': str(self.porcentagem),
            'status': self.status
        }

class DescontoProduto(db.Model):
    __tablename__ = 'desconto_produto'
    desconto_id_desconto = db.Column(db.Integer, db.ForeignKey('desconto.id_desconto'), primary_key=True)
    produto_idproduto = db.Column(db.Integer, db.ForeignKey('produto.idproduto'), primary_key=True)
    desconto = db.relationship('Desconto')
    produto = db.relationship('Produto')
    def to_json(self):
        return {
            'desconto_id_desconto': self.desconto_id_desconto,
            'produto_idproduto': self.produto_idproduto
        }

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

    def to_json(self):
        data_criacao_formatada = self.data_criacao.isoformat() if self.data_criacao is not None else None
        data_modificacao_formatada = self.data_modificado.isoformat() if self.data_modificado is not None else None        
        return {
            "idusuario": self.idusuario,
            "nome": self.nome,
            "login":self.login,
            "senha":self.senha,
            "celular":self.celular,
            "email":self.email,
            "status":self.status,
            "data_criacao":data_criacao_formatada,
            "data_modificado":data_modificacao_formatada,
            "perfil_idperfil":self.perfil_idperfil,
        }
    
class ItemCarrinho(db.Model):
    __tablename__ = 'item_carrinho'
    idproduto = db.Column(db.Integer, db.ForeignKey('produto.idproduto'), primary_key=True)
    idusuario = db.Column(db.Integer, db.ForeignKey('usuario.idusuario'), primary_key=True)
    idcompra = db.Column(db.Integer, db.ForeignKey('compra.idcompra'), primary_key=True)

    produto = db.relationship('Produto')
    usuario = db.relationship('Usuario')
    compra = db.relationship('Compra')
    def to_json(self):
        return {
            'idproduto': self.idproduto,
            'idusuario': self.idusuario,
            'idcompra': self.idcompra
        }
    
class MenuHasPerfil(db.Model):
    __tablename__ = 'menu_has_perfil'
    menu_idmenu = db.Column(db.Integer, db.ForeignKey('menu.idmenu'), primary_key=True)
    perfil_idperfil = db.Column(db.Integer, db.ForeignKey('perfil.idperfil'), primary_key=True)

    menu = db.relationship('Menu')
    perfil = db.relationship('Perfil')
    def to_json(self):
        return {
            'menu_idmenu': self.menu_idmenu,
            'perfil_idperfil': self.perfil_idperfil
        }