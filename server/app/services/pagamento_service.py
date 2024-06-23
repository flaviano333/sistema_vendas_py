from app.models import Pagamento
from app import db

def create_pagamento(data):
    novo_pagamento = Pagamento(
        tipo=data.get('tipo'),
        status=data.get('status')
    )
    db.session.add(novo_pagamento)
    db.session.commit()
    return novo_pagamento

def get_all_pagamentos():
    return Pagamento.query.all()

def get_pagamento_by_id(id):
    return Pagamento.query.get(id)

def update_pagamento(pagamento, data):
    pagamento.tipo = data.get('tipo', pagamento.tipo)
    pagamento.status = data.get('status', pagamento.status)
    db.session.commit()
    return pagamento

def delete_pagamento(id):
    pagamento = get_pagamento_by_id(id)
    if pagamento:
        db.session.delete(pagamento)
        db.session.commit()
        return pagamento
    return None
