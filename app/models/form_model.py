from app.extensions import db

class ContactFormModel(db.Model):
    __tablename__ = 'contact_form'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    campo_nuevo = db.Column(db.String(100))  # <-- Nuevo campo
