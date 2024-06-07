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
            "data_modificacao":data_modificacao_formatada,
            "perfil_idperfil":self.perfil_idperfil,
        }

class Perfil(db.Model):
    __tablename__ = 'perfil'

    idperfil = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(100), nullable=False)

    # Relacionamento reverso com a tabela usuario
    usuarios = relationship("Usuario", back_populates="perfil")

#selecionar
@app.route("/usuarios", methods=["GET"])
def seleciona_usuarios():
    usuarios_objetos = Usuario.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    return Response(json.dumps(usuarios_json))



app.run()