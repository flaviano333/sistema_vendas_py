from flask import Blueprint, jsonify, request, Response, current_app
from app.services.estoque_service import*
from app.utils import gera_response
import json

bp = Blueprint('estoque', __name__, url_prefix='/estoque')

@bp.route("/", methods=["GET"])
def seleciona_estoques():
    estoque_objetos = get_all_estoque()
    estoque_json = [estoque.to_json() for estoque in estoque_objetos]
    return gera_response(200, "estoque", estoque_json)

@bp.route("/<int:id>", methods=["GET"])
def seleciona_estoque(id):
    estoque_objeto = get_estoque_by_id(id)
    if not estoque_objeto:
        return gera_response(404, "estoque", {}, "Estoque não encontrado")
    estoque_json = estoque_objeto.to_json()
    return gera_response(200, "estoque", estoque_json)

@bp.route("/<int:id>", methods=["PUT"])
def atualizar_estoque(id):
    estoque_objeto = get_estoque_by_id(id)
    if not estoque_objeto:
        return gera_response(404, "estoque", {}, "Estoque não encontrado")

    body = request.get_json()
    try:
        estoque_atualizado = update_estoque(estoque_objeto, body)
        return gera_response(200, "estoque", estoque_atualizado.to_json(), "Alterado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "estoque", {}, "ERRO")

@bp.route("/", methods=["POST"])
def create_estoque_route():
    data = request.get_json()
    try:
        estoque = create_estoque(data)
        return jsonify(estoque.to_json()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400  

@bp.route("/<int:id>", methods=["DELETE"]) 
def deletar_estoque(id):
    try:
        estoque_deletado = delete_estoque(id)
        return gera_response(200, "estoque", estoque_deletado.to_json(), "Deletado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "estoque", {}, "ERRO") 