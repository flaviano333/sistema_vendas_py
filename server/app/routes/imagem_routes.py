from flask import Blueprint, jsonify, request
from app.services.imagem_service import *
from app.utils import gera_response

bp = Blueprint('imagem', __name__, url_prefix='/imagem')

@bp.route("/", methods=["GET"])
def get_imagens():
    imagens = get_all_imagens()
    imagens_json = [imagem.to_json() for imagem in imagens]
    return gera_response(200, "imagens", imagens_json)

@bp.route("/<int:id>", methods=["GET"])
def get_imagem(id):
    imagem = get_imagem_by_id(id)
    if not imagem:
        return gera_response(404, "imagem", {}, "Imagem não encontrada")
    return gera_response(200, "imagem", imagem.to_json())

@bp.route("/", methods=["POST"])
def create_imagem_route():
    data = request.get_json()
    try:
        imagem = create_imagem(data)
        return jsonify(imagem.to_json()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:id>", methods=["PUT"])
def update_imagem_route(id):
    imagem = get_imagem_by_id(id)
    if not imagem:
        return gera_response(404, "imagem", {}, "Imagem não encontrada")
    data = request.get_json()
    try:
        imagem_atualizada = update_imagem(imagem, data)
        return gera_response(200, "imagem", imagem_atualizada.to_json(), "Alterado com sucesso")
    except Exception as e:
        return gera_response(400, "imagem", {}, "ERRO")

@bp.route("/<int:id>", methods=["DELETE"])
def delete_imagem_route(id):
    try:
        imagem_deletada = delete_imagem(id)
        if not imagem_deletada:
            return gera_response(404, "imagem", {}, "Imagem não encontrada")
        return gera_response(200, "imagem", imagem_deletada.to_json(), "Deletado com sucesso")
    except Exception as e:
        return gera_response(400, "imagem", {}, "ERRO")
