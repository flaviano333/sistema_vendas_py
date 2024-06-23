from flask import Blueprint, jsonify, request
from app.services.pagamento_service import *
from app.utils import gera_response

bp = Blueprint('pagamento', __name__, url_prefix='/pagamento')

@bp.route("/", methods=["GET"])
def get_pagamentos():
    pagamentos = get_all_pagamentos()
    pagamentos_json = [pagamento.to_json() for pagamento in pagamentos]
    return gera_response(200, "pagamentos", pagamentos_json)

@bp.route("/<int:id>", methods=["GET"])
def get_pagamento(id):
    pagamento = get_pagamento_by_id(id)
    if not pagamento:
        return gera_response(404, "pagamento", {}, "Pagamento não encontrado")
    return gera_response(200, "pagamento", pagamento.to_json())

@bp.route("/", methods=["POST"])
def create_pagamento_route():
    data = request.get_json()
    try:
        pagamento = create_pagamento(data)
        return jsonify(pagamento.to_json()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/<int:id>", methods=["PUT"])
def update_pagamento_route(id):
    pagamento = get_pagamento_by_id(id)
    if not pagamento:
        return gera_response(404, "pagamento", {}, "Pagamento não encontrado")
    data = request.get_json()
    try:
        pagamento_atualizado = update_pagamento(pagamento, data)
        return gera_response(200, "pagamento", pagamento_atualizado.to_json(), "Alterado com sucesso")
    except Exception as e:
        return gera_response(400, "pagamento", {}, "ERRO")

@bp.route("/<int:id>", methods=["DELETE"])
def delete_pagamento_route(id):
    try:
        pagamento_deletado = delete_pagamento(id)
        if not pagamento_deletado:
            return gera_response(404, "pagamento", {}, "Pagamento não encontrado")
        return gera_response(200, "pagamento", pagamento_deletado.to_json(), "Deletado com sucesso")
    except Exception as e:
        return gera_response(400, "pagamento", {}, "ERRO")
