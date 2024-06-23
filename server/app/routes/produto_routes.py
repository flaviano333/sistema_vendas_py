from flask import Blueprint, jsonify, request, Response, current_app
from app.services.produto_service import*
from app.utils import gera_response
import json

bp = Blueprint('produto', __name__, url_prefix='/produto')

@bp.route("/", methods=["GET"])
def seleciona_produtos():
    produto_objetos = get_all_produto()
    produto_json = [produto.to_json() for produto in produto_objetos]
    return gera_response(200, "produto", produto_json)

@bp.route("/<int:id>", methods=["GET"])
def seleciona_produto(id):
    produto_objeto = get_produto_by_id(id)
    if not produto_objeto:
        return gera_response(404, "produto", {}, "Produto não encontrado")
    categoria_json = produto_objeto.to_json()
    return gera_response(200, "estoque", produto_json)

@bp.route("/<int:id>", methods=["PUT"])
def atualizar_produto(id):
    produto_objeto = get_produto_by_id(id)
    if not produto_objeto:
        return gera_response(404, "produto", {}, "Produto não encontrado")

    body = request.get_json()
    try:
        produto_atualizado = update_produto(produto_objeto, body)
        return gera_response(200, "produto", produto_atualizado.to_json(), "Alterado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "produto", {}, "ERRO")
    
@bp.route("/", methods=["POST"])
def create_produto_route():
    data = request.get_json()
    try:
        produto = create_produto(data)
        return jsonify(produto.to_json()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400  
    
@bp.route("/<int:id>", methods=["DELETE"]) 
def deletar_produto(id):
    try:
        produto_deletado = delete_produto(id)
        return gera_response(200, "produto", produto_deletado.to_json(), "Deletado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "estoque", {}, "ERRO") 
    