from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/sys_ecommerce_db'

db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    __table_args__ = (
        UniqueConstraint('login', name='login_UNIQUE'),
        UniqueConstraint('email', name='email_UNIQUE'),
        UniqueConstraint('celular', name='celular_UNIQUE'),
        db.Index('fk_usuario_perfil1_idx', 'perfil_idperfil')
    )

    idusuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(45), nullable=False)
    login = db.Column(db.String(20), nullable=False, unique=True)
    senha = db.Column(db.String(45), nullable=False)
    celular = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    status = db.Column(db.Boolean, nullable=False)
    data_criacao = db.Column(db.Date, nullable=False, default=date.today)
    data_modificado = db.Column(db.Date, nullable=False, default=date.today)
    perfil_idperfil = db.Column(db.Integer, ForeignKey('perfil.idperfil'), primary_key=True)

    # Definindo o relacionamento com a tabela perfil
    perfil = relationship("Perfil", back_populates="usuarios")
    
    def to_json(self):
        data_criacao_formatada = self.data_criacao.isoformat() if self.data_criacao is not None else None
        data_modificacao_formatada = self.data_modificado.isoformat() if self.data_modificado is not None else None        
        return {
            "idusuario": self.idusuario,
            "nome": self.nome,
            "login":self.login,
            "senha":self.senha,
            "celular":self.celular,
            "email":self.email,
            "status":self.status,
            "data_criacao":data_criacao_formatada,
            "data_modificado":data_modificacao_formatada,
            "perfil_idperfil":self.perfil_idperfil,
        }

class Perfil(db.Model):
    __tablename__ = 'perfil'

    idperfil = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(100), nullable=False)

    # Relacionamento reverso com a tabela usuario
    usuarios = relationship("Usuario", back_populates="perfil")

def gera_response(status, nome_do_conteudo, conteudo, mensagem = False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status = status, mimetype="application/json")

#selecionar todos
@app.route("/usuarios", methods=["GET"])
def seleciona_usuarios():
    usuarios_objetos = Usuario.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    return gera_response(200, "usuarios", usuarios_json)

#selecionar um
@app.route("/usuario/<id>")
def seleciona_usuario(id):
    usuario_objeto = Usuario.query.filter_by(idusuario = id).first()
    usuario_json = usuario_objeto.to_json()
    return gera_response(200, "usuario", usuario_json)

#criar usuario
@app.route("/usuario", methods=["POST"])
def cria_usuario():
    body = request.get_json()

    try:
        usuario = Usuario(nome = body["nome"],
                          login = body["login"],
                          senha = body["senha"],
                          celular = body["celular"],
                          email = body["email"],
                          status = body["status"],
                          data_criacao = body["data_criacao"],
                          data_modificado = body["data_modificado"],
                          perfil_idperfil = body["perfil_idperfil"]
                          )
        db.session.add(usuario)
        db.session.commit()
        return gera_response(201, "usuario", usuario.to_json(), "Cadastrado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "usuario", {}, "ERRO")

#atualizar usuario
@app.route("/usuario/<id>", methods=["PUT"])
def atualizar_usuario(id):
    usuario_objeto = Usuario.query.filter_by(idusuario=id).first()
    body = request.get_json()

    try:
        if('nome' in body):
            usuario_objeto.nome = body['nome']

        if('login' in body):
            usuario_objeto.login = body['login']

        if('senha' in  body):
            usuario_objeto.senha = body['senha']

        if('celular' in body):
            usuario_objeto.celular = body['celular']

        if('email' in body):
            usuario_objeto.email = body['email']

        if('status' in body):
            usuario_objeto.status = body['status']

        if('data_criacao' in body):
            usuario_objeto.data_criacao = body['data_criacao']

        if('data_modificado' in body):
            usuario_objeto.data_modificado = body['data_modificado']

        if('perfil_idperfil' in body):
            usuario_objeto.perfil_idperfil = body['perfil_idperfil']

        db.session.add(usuario_objeto)
        db.session.commit()
        return gera_response(200, "usuario", usuario_objeto.to_json(), "Alterado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "usuario", {}, "ERRO")
    
#deletar usuario

    
app.run()