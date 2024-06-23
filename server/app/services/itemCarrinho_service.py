from app.models import ItemCarrinho
from app import db

def create_item_carrinho(data):
    novo_item_carrinho = ItemCarrinho(
        idproduto=data.get('idproduto'),
        idusuario=data.get('idusuario'),
        idcompra=data.get('idcompra')
    )
    db.session.add(novo_item_carrinho)
    db.session.commit()
    return novo_item_carrinho

def get_all_item_carrinho():
    return ItemCarrinho.query.all()

def get_item_carrinho_by_ids(produto_id, usuario_id, compra_id):
    return ItemCarrinho.query.filter_by(idproduto=produto_id, idusuario=usuario_id, idcompra=compra_id).first()

def delete_item_carrinho(produto_id, usuario_id, compra_id):
    item_carrinho = get_item_carrinho_by_ids(produto_id, usuario_id, compra_id)
    if item_carrinho:
        db.session.delete(item_carrinho)
        db.session.commit()
        return item_carrinho
    return None
