from flask import Blueprint, jsonify, request
from app.services.itemCarrinho_service import *
from app.utils import gera_response

bp = Blueprint('item_carrinho', __name__, url_prefix='/item_carrinho')

@bp.route("/", methods=["GET"])
def get_item_carrinhos():
    item_carrinhos = get_all_item_carrinho()
    item_carrinhos_json = [item.to_json() for item in item_carrinhos]
    return gera_response(200, "item_carrinhos", item_carrinhos_json)

@bp.route("/", methods=["POST"])
def create_item_carrinho_route():
    data = request.get_json()
    try:
        item_carrinho = create_item_carrinho(data)
        return jsonify(item_carrinho.to_json()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:produto_id>/<int:usuario_id>/<int:compra_id>", methods=["DELETE"])
def delete_item_carrinho_route(produto_id, usuario_id, compra_id):
    try:
        item_carrinho_deletado = delete_item_carrinho(produto_id, usuario_id, compra_id)
        if not item_carrinho_deletado:
            return gera_response(404, "item_carrinho", {}, "ItemCarrinho não encontrado")
        return gera_response(200, "item_carrinho", item_carrinho_deletado.to_json(), "Deletado com sucesso")
    except Exception as e:
        return gera_response(400, "item_carrinho", {}, "ERRO")
