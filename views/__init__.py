from views.accesorios import accesorio_app_bp
from views.marca import marca_app_bp
from views.tipo import tipo_app_bp
from views.stock import stock_app_bp
from views.telefono import telefono_app_bp
from views.main import main_app_bp
from views.auth import auth_bp


def register_blueprint(app):
    
    app.register_blueprint(accesorio_app_bp)
    app.register_blueprint(marca_app_bp)
    app.register_blueprint(tipo_app_bp)
    app.register_blueprint(stock_app_bp)
    app.register_blueprint(telefono_app_bp)
    app.register_blueprint(main_app_bp)
    app.register_blueprint(auth_bp)