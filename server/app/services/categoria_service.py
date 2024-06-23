from app.models import Categoria
from app import db

def get_all_categoria():
    return Categoria.query.all()

def get_categoria_by_id(id):
    return Categoria.query.filter_by(idcategoria=id).first()

def update_categoria(categoria_objeto, data):
    if 'nome_categoria' in data:
        categoria_objeto.nome_categoria = data['nome_categoria']
    if 'descricao' in data:
        categoria_objeto.descricao = data['descricao']

    db.session.commit()
    return categoria_objeto

def create_categoria(data):
    categoria = Categoria(
        nome_categoria=data['nome_categoria'],
        descricao=data['descricao'],
    )
    db.session.add(categoria)
    db.session.commit()
    return categoria

def delete_categoria(id):
    cadegoria_objeto = Categoria.query.filter_by(idcategoria=id).first()
    db.session.delete(cadegoria_objeto)
    db.session.commit()    
    return cadegoria_objeto