from flask import Blueprint, jsonify, request
from app.services.menu_service import *
from app.utils import gera_response

bp = Blueprint('menu', __name__, url_prefix='/menu')

@bp.route("/", methods=["GET"])
def get_menus():
    menus = get_all_menus()
    menus_json = [menu.to_json() for menu in menus]
    return gera_response(200, "menus", menus_json)

@bp.route("/<int:id>", methods=["GET"])
def get_menu(id):
    menu = get_menu_by_id(id)
    if not menu:
        return gera_response(404, "menu", {}, "Menu não encontrado")
    return gera_response(200, "menu", menu.to_json())

@bp.route("/", methods=["POST"])
def create_menu_route():
    data = request.get_json()
    try:
        menu = create_menu(data)
        return jsonify(menu.to_json()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:id>", methods=["PUT"])
def update_menu_route(id):
    menu = get_menu_by_id(id)
    if not menu:
        return gera_response(404, "menu", {}, "Menu não encontrado")
    data = request.get_json()
    try:
        menu_atualizado = update_menu(menu, data)
        return gera_response(200, "menu", menu_atualizado.to_json(), "Alterado com sucesso")
    except Exception as e:
        return gera_response(400, "menu", {}, "ERRO")

@bp.route("/<int:id>", methods=["DELETE"])
def delete_menu_route(id):
    try:
        menu_deletado = delete_menu(id)
        if not menu_deletado:
            return gera_response(404, "menu", {}, "Menu não encontrado")
        return gera_response(200, "menu", menu_deletado.to_json(), "Deletado com sucesso")
    except Exception as e:
        return gera_response(400, "menu", {}, "ERRO")

