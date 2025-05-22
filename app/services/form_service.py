from app.models.form_model import ContactFormModel
from app.extensions import db

def save_form_data(name, email, message, nuevo_campo=None):
    form_entry = ContactFormModel(name=name, email=email, message=message, campo_nuevo=nuevo_campo)
    db.session.add(form_entry)
    db.session.commit()
    return form_entry
