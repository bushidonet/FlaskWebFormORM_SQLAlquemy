from flask import Flask
from .extensions import db, migrate
from .routes.form_route import form_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    db.init_app(app)
    migrate.init_app(app, db)  # 👈 necesario
    app.register_blueprint(form_bp)  # 👈 esto es clave
    return app