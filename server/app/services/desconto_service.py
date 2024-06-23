from app.models import Desconto
from app import db

def create_desconto(data):
    novo_desconto = Desconto(
        descricao=data.get('descricao'),
        porcentagem=data.get('porcentagem'),
        status=data.get('status', True)
    )
    db.session.add(novo_desconto)
    db.session.commit()
    return novo_desconto

def get_all_descontos():
    return Desconto.query.all()

def get_desconto_by_id(id):
    return Desconto.query.get(id)

def update_desconto(desconto, data):
    desconto.descricao = data.get('descricao', desconto.descricao)
    desconto.porcentagem = data.get('porcentagem', desconto.porcentagem)
    desconto.status = data.get('status', desconto.status)
    db.session.commit()
    return desconto

def delete_desconto(id):
    desconto = get_desconto_by_id(id)
    if desconto:
        db.session.delete(desconto)
        db.session.commit()
        return desconto
    return None
