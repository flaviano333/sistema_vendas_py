from app.models import Menu
from app import db

def create_menu(data):
    novo_menu = Menu(
        menu=data.get('menu'),
        link=data.get('link')
    )
    db.session.add(novo_menu)
    db.session.commit()
    return novo_menu

def get_all_menus():
    return Menu.query.all()

def get_menu_by_id(id):
    return Menu.query.get(id)

def update_menu(menu, data):
    menu.menu = data.get('menu', menu.menu)
    menu.link = data.get('link', menu.link)
    db.session.commit()
    return menu

def delete_menu(id):
    menu = get_menu_by_id(id)
    if menu:
        db.session.delete(menu)
        db.session.commit()
        return menu
    return None
