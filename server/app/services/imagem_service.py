from datetime import date
from app.models import Imagem
from app import db

def create_imagem(data):
    nova_imagem = Imagem(
        nome=data.get('nome'),
        caminho=data.get('caminho'),
        idproduto=data.get('idproduto')
    )
    db.session.add(nova_imagem)
    db.session.commit()
    return nova_imagem

def get_all_imagens():
    return Imagem.query.all()

def get_imagem_by_id(id):
    return Imagem.query.get(id)

def update_imagem(imagem, data):
    imagem.nome = data.get('nome', imagem.nome)
    imagem.caminho = data.get('caminho', imagem.caminho)
    imagem.data_modificado = date.today()
    db.session.commit()
    return imagem

def delete_imagem(id):
    imagem = get_imagem_by_id(id)
    if imagem:
        db.session.delete(imagem)
        db.session.commit()
        return imagem
    return None
