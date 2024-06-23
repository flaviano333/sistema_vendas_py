from app.models import Estoque
from app import db

def get_all_estoque():
    return Estoque.query.all()

def get_estoque_by_id(id):
    return Estoque.query.filter_by(idestoque=id).first()

def update_estoque(estoque_objeto, data):
    if 'quantidade' in data:
        estoque_objeto.quantidade = data['quantidade']
    if 'data_criacao' in data:
        estoque_objeto.data_criacao = data['data_criacao']
    if 'data_modificado' in data:
        estoque_objeto.data_modificado = data['data_modificado']

    db.session.commit()
    return estoque_objeto

def create_estoque(data):
    estoque = Estoque(
        quantidade=data['quantidade'],
        data_criacao=data['data_criacao'],
        data_modificado=data['data_modificado'],
    )
    db.session.add(estoque)
    db.session.commit()
    return estoque

def delete_estoque(id):
    estoque_objeto = Estoque.query.filter_by(idestoque=id).first()
    db.session.delete(estoque_objeto)
    db.session.commit()    
    return estoque_objeto