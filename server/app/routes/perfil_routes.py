from flask import Blueprint, jsonify, request
from app.services.perfil_service import *
from app.utils import gera_response

bp = Blueprint('perfil', __name__, url_prefix='/perfil')

@bp.route("/", methods=["GET"])
def get_perfis():
    perfis = get_all_perfis()
    perfis_json = [perfil.to_json() for perfil in perfis]
    return gera_response(200, "perfis", perfis_json)

@bp.route("/<int:id>", methods=["GET"])
def get_perfil(id):
    perfil = get_perfil_by_id(id)
    if not perfil:
        return gera_response(404, "perfil", {}, "Perfil não encontrado")
    return gera_response(200, "perfil", perfil.to_json())

@bp.route("/", methods=["POST"])
def create_perfil_route():
    data = request.get_json()
    try:
        perfil = create_perfil(data)
        return jsonify(perfil.to_json()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:id>", methods=["PUT"])
def update_perfil_route(id):
    perfil = get_perfil_by_id(id)
    if not perfil:
        return gera_response(404, "perfil", {}, "Perfil não encontrado")
    data = request.get_json()
    try:
        perfil_atualizado = update_perfil(perfil, data)
        return gera_response(200, "perfil", perfil_atualizado.to_json(), "Alterado com sucesso")
    except Exception as e:
        return gera_response(400, "perfil", {}, "ERRO")

@bp.route("/<int:id>", methods=["DELETE"])
def delete_perfil_route(id):
    try:
        perfil_deletado = delete_perfil(id)
        if not perfil_deletado:
            return gera_response(404, "perfil", {}, "Perfil não encontrado")
        return gera_response(200, "perfil", perfil_deletado.to_json(), "Deletado com sucesso")
    except Exception as e:
        return gera_response(400, "perfil", {}, "ERRO")
