from app.models import MenuHasPerfil
from app import db

def create_menu_has_perfil(data):
    novo_menu_has_perfil = MenuHasPerfil(
        menu_idmenu=data.get('menu_idmenu'),
        perfil_idperfil=data.get('perfil_idperfil')
    )
    db.session.add(novo_menu_has_perfil)
    db.session.commit()
    return novo_menu_has_perfil

def get_all_menu_has_perfil():
    return MenuHasPerfil.query.all()

def get_menu_has_perfil_by_ids(menu_id, perfil_id):
    return MenuHasPerfil.query.filter_by(menu_idmenu=menu_id, perfil_idperfil=perfil_id).first()

def delete_menu_has_perfil(menu_id, perfil_id):
    menu_has_perfil = get_menu_has_perfil_by_ids(menu_id, perfil_id)
    if menu_has_perfil:
        db.session.delete(menu_has_perfil)
        db.session.commit()
        return menu_has_perfil
    return None

