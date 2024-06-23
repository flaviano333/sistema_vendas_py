from app.models import Produto
from app import db

def get_all_produto():
    return Produto.query.all()

def get_produto_by_id(id):
    return Produto.query.filter_by(idproduto=id).first()

def update_produto(produto_objeto, data):
    if 'nome_produto' in data:
        produto_objeto.nome_produto = data['nome_produto']
    if 'status' in data:
        produto_objeto.status = data['status']
    if 'link' in data:
        produto_objeto.link = data['link']
    if 'preco' in data:
        produto_objeto.preco = data['preco']
    if 'idestoque' in data:
        produto_objeto.status = data['idestoque']
    if 'categoria_idcatergoria' in data:
        produto_objeto.categoria_idcatergoria = data['categoria_idcatergoria']                        
    db.session.commit()
    return produto_objeto

def create_produto(data):
    produto = Produto(
        nome_produto=data['nome_produto'],
        status=data['status'],
        link=data['link'],
        preco=data['preco'],
        idestoque=data['idestoque'],
        categoria_idcatergoria=data['categoria_idcatergoria'],
    )
    db.session.add(produto)
    db.session.commit()
    return produto

def delete_produto(id):
    produto_objeto = Produto.query.filter_by(idproduto=id).first()
    db.session.delete(produto_objeto)
    db.session.commit()    
    return produto_objeto