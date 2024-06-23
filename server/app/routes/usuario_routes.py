from flask import Blueprint, jsonify, request, Response, current_app
from app.services.usuario_service import*
from app.utils import gera_response
import json

bp = Blueprint('usuario', __name__, url_prefix='/usuarios')

@bp.route("/", methods=["GET"])
def seleciona_usuarios():
    usuarios_objetos = get_all_usuarios()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    return gera_response(200, "usuarios", usuarios_json)

@bp.route("/<int:id>", methods=["GET"])
def seleciona_usuario(id):
    usuario_objeto = get_usuario_by_id(id)
    if not usuario_objeto:
        return gera_response(404, "usuario", {}, "Usuário não encontrado")
    usuario_json = usuario_objeto.to_json()
    return gera_response(200, "usuario", usuario_json)

@bp.route("/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    usuario_objeto = get_usuario_by_id(id)
    if not usuario_objeto:
        return gera_response(404, "usuario", {}, "Usuário não encontrado")

    body = request.get_json()
    try:
        usuario_atualizado = update_usuario(usuario_objeto, body)
        return gera_response(200, "usuario", usuario_atualizado.to_json(), "Alterado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "usuario", {}, "ERRO")

@bp.route("/", methods=["POST"])
def create_usuario_route():
    data = request.get_json()
    try:
        usuario = create_usuario(data)
        return jsonify(usuario.to_json()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400  

@bp.route("/<int:id>", methods=["DELETE"]) 
def deletar_usuario(id):
    try:
        usuario_deletado = delete_usuario(id)
        return gera_response(200, "usuario", usuario_deletado.to_json(), "Deletado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "usuario", {}, "ERRO")    
        