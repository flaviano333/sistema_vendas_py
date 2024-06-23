from app.models import DescontoProduto
from app import db

def create_desconto_produto(data):
    novo_desconto_produto = DescontoProduto(
        desconto_id_desconto=data.get('desconto_id_desconto'),
        produto_idproduto=data.get('produto_idproduto')
    )
    db.session.add(novo_desconto_produto)
    db.session.commit()
    return novo_desconto_produto

def get_all_desconto_produto():
    return DescontoProduto.query.all()

def get_desconto_produto_by_ids(desconto_id, produto_id):
    return DescontoProduto.query.filter_by(desconto_id_desconto=desconto_id, produto_idproduto=produto_id).first()

def delete_desconto_produto(desconto_id, produto_id):
    desconto_produto = get_desconto_produto_by_ids(desconto_id, produto_id)
    if desconto_produto:
        db.session.delete(desconto_produto)
        db.session.commit()
        return desconto_produto
    return None
