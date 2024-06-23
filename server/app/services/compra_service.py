from app.models import Compra
from app import db

def create_compra(data):
    nova_compra = Compra(
        valor_total=data.get('valor_total'),
        status=data.get('status'),
        descricao=data.get('descricao'),
        idpagamento=data.get('idpagamento')
    )
    db.session.add(nova_compra)
    db.session.commit()
    return nova_compra

def get_all_compras():
    return Compra.query.all()

def get_compra_by_id(id):
    return Compra.query.get(id)

def update_compra(compra, data):
    compra.valor_total = data.get('valor_total', compra.valor_total)
    compra.status = data.get('status', compra.status)
    compra.descricao = data.get('descricao', compra.descricao)
    compra.idpagamento = data.get('idpagamento', compra.idpagamento)
    db.session.commit()
    return compra

def delete_compra(id):
    compra = get_compra_by_id(id)
    if compra:
        db.session.delete(compra)
        db.session.commit()
        return compra
    return None
