from app.models import Usuario
from app import db

def get_all_usuarios():
    return Usuario.query.all()

def get_usuario_by_id(id):
    return Usuario.query.filter_by(idusuario=id).first()

def update_usuario(usuario_objeto, data):
    if 'nome' in data:
        usuario_objeto.nome = data['nome']
    if 'login' in data:
        usuario_objeto.login = data['login']
    if 'senha' in data:
        usuario_objeto.senha = data['senha']
    if 'celular' in data:
        usuario_objeto.celular = data['celular']
    if 'email' in data:
        usuario_objeto.email = data['email']
    if 'status' in data:
        usuario_objeto.status = data['status']
    if 'data_criacao' in data:
        usuario_objeto.data_criacao = data['data_criacao']
    if 'data_modificado' in data:
        usuario_objeto.data_modificado = data['data_modificado']
    if 'perfil_idperfil' in data:
        usuario_objeto.perfil_idperfil = data['perfil_idperfil']

    db.session.commit()
    return usuario_objeto

def create_usuario(data):
    usuario = Usuario(
        nome=data['nome'],
        login=data['login'],
        senha=data['senha'],
        celular=data.get('celular'),
        email=data.get('email'),
        status=data['status'],
        data_criacao=data['data_criacao'],
        data_modificado=data['data_modificado'],
        perfil_idperfil=data['perfil_idperfil']
    )
    db.session.add(usuario)
    db.session.commit()
    return usuario

def delete_usuario(id):
    usuario_objeto = Usuario.query.filter_by(idusuario=id).first()
    db.session.delete(usuario_objeto)
    db.session.commit()    
    return usuario_objeto

