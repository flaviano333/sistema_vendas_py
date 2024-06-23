from flask import Blueprint, jsonify, request
from app.services.descontoProduto_service import *
from app.utils import gera_response

bp = Blueprint('desconto_produto', __name__, url_prefix='/desconto_produto')

@bp.route("/", methods=["GET"])
def get_desconto_produtos():
    desconto_produtos = get_all_desconto_produto()
    desconto_produtos_json = [dp.to_json() for dp in desconto_produtos]
    return gera_response(200, "desconto_produtos", desconto_produtos_json)

@bp.route("/", methods=["POST"])
def create_desconto_produto_route():
    data = request.get_json()
    try:
        desconto_produto = create_desconto_produto(data)
        return jsonify(desconto_produto.to_json()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:desconto_id>/<int:produto_id>", methods=["DELETE"])
def delete_desconto_produto_route(desconto_id, produto_id):
    try:
        desconto_produto_deletado = delete_desconto_produto(desconto_id, produto_id)
        if not desconto_produto_deletado:
            return gera_response(404, "desconto_produto", {}, "DescontoProduto não encontrado")
        return gera_response(200, "desconto_produto", desconto_produto_deletado.to_json(), "Deletado com sucesso")
    except Exception as e:
        return gera_response(400, "desconto_produto", {}, "ERRO")
