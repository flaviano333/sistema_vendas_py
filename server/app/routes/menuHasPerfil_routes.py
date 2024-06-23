from flask import Blueprint, jsonify, request
from app.services.menuHasPerfil_service import *
from app.utils import gera_response

bp = Blueprint('menu_has_perfil', __name__, url_prefix='/menu_has_perfil')

@bp.route("/", methods=["GET"])
def get_menu_has_perfils():
    menu_has_perfils = get_all_menu_has_perfil()
    menu_has_perfils_json = [item.to_json() for item in menu_has_perfils]
    return gera_response(200, "menu_has_perfils", menu_has_perfils_json)

@bp.route("/", methods=["POST"])
def create_menu_has_perfil_route():
    data = request.get_json()
    try:
        menu_has_perfil = create_menu_has_perfil(data)
        return jsonify(menu_has_perfil.to_json()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:menu_id>/<int:perfil_id>", methods=["DELETE"])
def delete_menu_has_perfil_route(menu_id, perfil_id):
    try:
        menu_has_perfil_deletado = delete_menu_has_perfil(menu_id, perfil_id)
        if not menu_has_perfil_deletado:
            return gera_response(404, "menu_has_perfil", {}, "Associação não encontrada")
        return gera_response(200, "menu_has_perfil", menu_has_perfil_deletado.to_json(), "Deletado com sucesso")
    except Exception as e:
        return gera_response(400, "menu_has_perfil", {}, "ERRO")