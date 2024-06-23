from flask import Blueprint, jsonify, request, Response, current_app
from app.services.categoria_service import*
from app.utils import gera_response
import json

bp = Blueprint('categoria', __name__, url_prefix='/categoria')

@bp.route("/", methods=["GET"])
def seleciona_categorias():
    categoria_objetos = get_all_categoria()
    categoria_json = [categoria.to_json() for categoria in categoria_objetos]
    return gera_response(200, "categoria", categoria_json)

@bp.route("/<int:id>", methods=["GET"])
def seleciona_categoria(id):
    categoria_objeto = get_categoria_by_id(id)
    if not categoria_objeto:
        return gera_response(404, "categoria", {}, "Categoria não encontrada")
    categoria_json = categoria_objeto.to_json()
    return gera_response(200, "estoque", categoria_json)

@bp.route("/<int:id>", methods=["PUT"])
def atualizar_categoria(id):
    categoria_objeto = get_categoria_by_id(id)
    if not categoria_objeto:
        return gera_response(404, "categoria", {}, "Categoria não encontrada")

    body = request.get_json()
    try:
        categoria_atualizado = update_categoria(categoria_objeto, body)
        return gera_response(200, "categoria", categoria_atualizado.to_json(), "Alterada com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "estoque", {}, "ERRO")
    
@bp.route("/", methods=["POST"])
def create_categoria_route():
    data = request.get_json()
    try:
        categoria = create_categoria(data)
        return jsonify(categoria.to_json()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400  
    
@bp.route("/<int:id>", methods=["DELETE"]) 
def deletar_categoria(id):
    try:
        categoria_deletado = delete_categoria(id)
        return gera_response(200, "categoria", categoria_deletado.to_json(), "Deletada com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "estoque", {}, "ERRO") 
    