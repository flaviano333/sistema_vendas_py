from flask import Blueprint, jsonify, request
from app.services.desconto_service import *
from app.utils import gera_response

bp = Blueprint('desconto', __name__, url_prefix='/desconto')

@bp.route("/", methods=["GET"])
def get_descontos():
    descontos = get_all_descontos()
    descontos_json = [desconto.to_json() for desconto in descontos]
    return gera_response(200, "descontos", descontos_json)

@bp.route("/<int:id>", methods=["GET"])
def get_desconto(id):
    desconto = get_desconto_by_id(id)
    if not desconto:
        return gera_response(404, "desconto", {}, "Desconto não encontrado")
    return gera_response(200, "desconto", desconto.to_json())

@bp.route("/", methods=["POST"])
def create_desconto_route():
    data = request.get_json()
    try:
        desconto = create_desconto(data)
        return jsonify(desconto.to_json()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:id>", methods=["PUT"])
def update_desconto_route(id):
    desconto = get_desconto_by_id(id)
    if not desconto:
        return gera_response(404, "desconto", {}, "Desconto não encontrado")
    data = request.get_json()
    try:
        desconto_atualizado = update_desconto(desconto, data)
        return gera_response(200, "desconto", desconto_atualizado.to_json(), "Alterado com sucesso")
    except Exception as e:
        return gera_response(400, "desconto", {}, "ERRO")

@bp.route("/<int:id>", methods=["DELETE"])
def delete_desconto_route(id):
    try:
        desconto_deletado = delete_desconto(id)
        if not desconto_deletado:
            return gera_response(404, "desconto", {}, "Desconto não encontrado")
        return gera_response(200, "desconto", desconto_deletado.to_json(), "Deletado com sucesso")
    except Exception as e:
        return gera_response(400, "desconto", {}, "ERRO")
