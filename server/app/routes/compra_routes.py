from flask import Blueprint, jsonify, request
from app.services.compra_service import *
from app.utils import gera_response

bp = Blueprint('compra', __name__, url_prefix='/compra')

@bp.route("/", methods=["GET"])
def get_compras():
    compras = get_all_compras()
    compras_json = [compra.to_json() for compra in compras]
    return gera_response(200, "compras", compras_json)

@bp.route("/<int:id>", methods=["GET"])
def get_compra(id):
    compra = get_compra_by_id(id)
    if not compra:
        return gera_response(404, "compra", {}, "Compra não encontrada")
    return gera_response(200, "compra", compra.to_json())

@bp.route("/", methods=["POST"])
def create_compra_route():
    data = request.get_json()
    try:
        compra = create_compra(data)
        return jsonify(compra.to_json()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:id>", methods=["PUT"])
def update_compra_route(id):
    compra = get_compra_by_id(id)
    if not compra:
        return gera_response(404, "compra", {}, "Compra não encontrada")
    data = request.get_json()
    try:
        compra_atualizada = update_compra(compra, data)
        return gera_response(200, "compra", compra_atualizada.to_json(), "Alterado com sucesso")
    except Exception as e:
        return gera_response(400, "compra", {}, "ERRO")

@bp.route("/<int:id>", methods=["DELETE"])
def delete_compra_route(id):
    try:
        compra_deletada = delete_compra(id)
        if not compra_deletada:
            return gera_response(404, "compra", {}, "Compra não encontrada")
        return gera_response(200, "compra", compra_deletada.to_json(), "Deletado com sucesso")
    except Exception as e:
        return gera_response(400, "compra", {}, "ERRO")
