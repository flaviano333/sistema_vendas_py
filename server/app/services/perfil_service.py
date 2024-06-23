from app.models import Perfil
from app import db

def create_perfil(data):
    novo_perfil = Perfil(
        perfil=data.get('perfil')
    )
    db.session.add(novo_perfil)
    db.session.commit()
    return novo_perfil

def get_all_perfis():
    return Perfil.query.all()

def get_perfil_by_id(id):
    return Perfil.query.get(id)

def update_perfil(perfil, data):
    perfil.perfil = data.get('perfil', perfil.perfil)
    db.session.commit()
    return perfil

def delete_perfil(id):
    perfil = get_perfil_by_id(id)
    if perfil:
        db.session.delete(perfil)
        db.session.commit()
        return perfil
    return None